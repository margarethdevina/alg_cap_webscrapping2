# import library
from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def scrap(url):
    
    # buat cangkang
    popno = []
    titles = []
    imdb_ratings = []
    metascores = []
    votes = []   
    
    # untuk tarik data di page pertama karena format url beda, page lainnya dilooping terpisah
    url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&ref_=adv_nxt')
    soup = BeautifulSoup(url_get.content,"html.parser")
    lister = soup.find_all('div', attrs={'class':'lister-item-content'})
    if lister is not None:
      
    # ambil data per movie
        for onelist in lister:
    
            # berpatok ke metascore
            # kalau metascore ga none berarti isi masing2 kolom seperti apa?
            if onelist.find('div', class_ = 'inline-block ratings-metascore') is not None:
        
                # urutan
                urut = onelist.h3.span.text
                urut = urut.strip()
                popno.append(urut)
        
                # judul
                title = onelist.h3.a.text
                title = title.strip()
                titles.append(title)
        
                # imdb rating
                ratings = float(onelist.strong.text)
                imdb_ratings.append(ratings)
        
                # metascore dibagi 10 biar bandingin ke imdb rating lebih enak
                mscore = onelist.find('div', attrs={'class':'inline-block ratings-metascore'}).span.text
                mscore = int(mscore)/10
                metascores.append(float(mscore))
                    
                # votes, ambil data value langsung biar ga usa repot ilangin koma
                vote = onelist.find('span', attrs={'name':'nv'})['data-value']
                votes.append(int(vote))

            # kalau metascore none berarti isi masing2 kolom seperti apa?
            if onelist.find('div', class_ = 'inline-block ratings-metascore') is None:
        
                # urutan
                urut = onelist.h3.span.text
                urut = urut.strip()
                popno.append(urut)
        
                # judul
                title = onelist.h3.a.text
                title = title.strip()
                titles.append(title)
        
                # imdb rating
                ratings = float(onelist.strong.text)
                imdb_ratings.append(ratings)
            
                # metascore karena none type dan biar datanya bisa ketarik juga, di nol in aja
                mscore = 0.0
                metascores.append(float(mscore))
                    
                # votes
                vote = onelist.find('span', attrs={'name':'nv'})['data-value']
                votes.append(int(vote))
    
    # untuk tarik data di page kedua dst
    pages = [str(i) for i in range(51,150,50)]
    for page in pages:
        url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&start='+page+'&ref_=adv_nxt')
        soup = BeautifulSoup(url_get.content,"html.parser")
        lister = soup.find_all('div', attrs={'class':'lister-item-content'})
      
    # ambil data per movie
        for onelist in lister:
    
            # berpatok ke metascore
            # kalau metascore ga none berarti isi masing2 kolom seperti apa?
            if onelist.find('div', class_ = 'inline-block ratings-metascore') is not None:
        
                # urutan
                urut = onelist.h3.span.text
                urut = urut.strip()
                popno.append(urut)
        
                # judul
                title = onelist.h3.a.text
                title = title.strip()
                titles.append(title)
        
                # imdb rating
                ratings = float(onelist.strong.text)
                imdb_ratings.append(ratings)
        
                # metascore dibagi 10 biar bandingin ke imdb rating lebih enak
                mscore = onelist.find('div', attrs={'class':'inline-block ratings-metascore'}).span.text
                mscore = int(mscore)/10
                metascores.append(float(mscore))
                    
                # votes, ambil data value langsung biar ga usa repot ilangin koma
                vote = onelist.find('span', attrs={'name':'nv'})['data-value']
                votes.append(int(vote))

            # kalau metascore none berarti isi masing2 kolom seperti apa?
            if onelist.find('div', class_ = 'inline-block ratings-metascore') is None:
        
                # urutan
                urut = onelist.h3.span.text
                urut = urut.strip()
                popno.append(urut)
        
                # judul
                title = onelist.h3.a.text
                title = title.strip()
                titles.append(title)
        
                # imdb rating
                ratings = float(onelist.strong.text)
                imdb_ratings.append(ratings)
            
                # metascore karena none type dan biar datanya bisa ketarik juga, di nol in aja
                mscore = 0.0
                metascores.append(float(mscore))
                    
                # votes
                vote = onelist.find('span', attrs={'name':'nv'})['data-value']
                votes.append(int(vote))
        
    # dari cangkang yang dah dibuat disusun jadi df
    df = pd.DataFrame({
    'popularity_order': popno,
    'film_title': titles,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes
    })
    
    # ilangin titik di peringkat popularitas
    df['popularity_order'] = df['popularity_order'].replace('[\.]','',regex=True).astype('int64')
    
    # pas saya tarik masi nama korea jadi biar sesuai tampilan imdb di replace aja
    df['film_title'] = df['film_title'].replace('Gisaengchung','Parasite')
    
    # disortir ulang biar keurut sm tampilan imdb
    df = df.sort_values('popularity_order', ascending=True).set_index('popularity_order')

    return df

@app.route("/")
def index():
    df = scrap('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31') #insert url here

    # This part for rendering matplotlib
    fig = plt.figure(figsize=(5,2),dpi=300)
    
    # plot yg mau dishow cuma top 7 tingkat popularitas
    # untuk keperluan analisa sort value nya pakai imdb rating
    df.head(7).sort_values('imdb',ascending=False).set_index('film_title').\
    drop(columns=['metascore','votes']).\
    plot(kind='barh', width=0.5, align='center')
    
    # Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    # This part for rendering matplotlib

    # this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    # biar tampilan kesusun sesuai template dipanggil index_copy1 dari folder template
    return render_template("index_copy1.html", table=df, result=result)    
    
if __name__ == "__main__": 
    app.run(debug=True) # biar error log kelihatan