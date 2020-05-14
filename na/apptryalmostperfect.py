from flask import Flask, render_template 
import pandas as pd
import requests
from bs4 import BeautifulSoup 
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def scrap(url):
    #This is fuction for scrapping
    url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31')
    soup = BeautifulSoup(url_get.content,"html.parser")
    lister = soup.find_all('div', attrs={'class':'lister-item-content'})
    
    #Find the key to get the information
    # buat cangkang
    titles = []
    imdb_ratings = []
    metascores = []
    votes = []

    # ambil data per movie
    for onelist in lister:
    
        # berpatok ke metascore
        # kalau metascore ga none berarti isi masing2 kolom seperti apa?
        if onelist.find('div', class_ = 'inline-block ratings-metascore') is not None:
        
            # judul
            title = onelist.h3.a.text
            titles.append(title)
        
            # imdb rating
            ratings = float(onelist.strong.text)
            imdb_ratings.append(ratings)
        
            # metascore
            mscore = onelist.find('div', attrs={'class':'inline-block ratings-metascore'}).span.text
            metascores.append(int(mscore))
        
            # votes
            vote = onelist.find('span', attrs={'name':'nv'})['data-value']
            votes.append(int(vote))

        # kalau metascore none berarti isi masing2 kolom seperti apa?
        if onelist.find('div', class_ = 'inline-block ratings-metascore') is None:
        
            # judul
            title = onelist.h3.a.text
            titles.append(title)
        
            # imdb rating
            ratings = float(onelist.strong.text)
            imdb_ratings.append(ratings)
        
            # metascore
            mscore = 0
            metascores.append(int(mscore))
        
            # votes
            vote = onelist.find('span', attrs={'name':'nv'})['data-value']
            votes.append(int(vote))
        
    # dari cangkang yang dah dibuat disusun jadi df
    df = pd.DataFrame({
    'film_title': titles,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes
    })
    
    df = df[(df['imdb']>7)&(df['metascore']>70)].sort_values('votes', ascending=False).head(7)

    return df

@app.route("/")
def index():
    df = scrap('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31') #insert url here

    #This part for rendering matplotlib
    fig = plt.figure(figsize=(5,2),dpi=300)
    df.plot(kind='bar')
    
    #Do not change this part
    plt.savefig('plot1',bbox_inches="tight") 
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    #This part for rendering matplotlib

    #this is for rendering the table
    df = df.to_html(classes=["table table-bordered table-striped table-dark table-condensed"])

    return render_template("index_copy1.html", table=df, result=result)
    #except Exception as e: ga dipake karena exception harus ada try nya
    #    return str(e)

if __name__ == "__main__": 
    app.run(debug=True)