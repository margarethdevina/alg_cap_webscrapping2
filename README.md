# Aloha!

Salam kenal, saya Margareth Devina, salah satu student di Kappa Data Analytics di Algoritma.

Dalam penyelesaian studi data analytics, kami para student diharapkan bisa menyelesaikan sebuah capstone.

Capstone yg saya pilih adalah webscrapping website imdb untuk tahun 2019 dengan tampilan tersortir berdasarkan tingkat popularitasnya.

Berdasarkan hasil webscrapping yang dilakukan, kami ditargetkan untuk dapat menyediakan sebuah web berisi hasil render plot berdasarkan 7 film paling populer di tahun 2019 disertai dengan table dataframe untuk keterangan lebih detil dari plot itu.

Tentunya pembuatan plot tersebut didukung dengan analisis, dan berikut analisis saya:

>Selama ini saya selalu berpikir film paling populer pasti memiliki rating yg tinggi. Tapi ternyata tidak begitu...ada yg rating imdb nya <7 bahkan beberapa ada yang memiliki metascore <6 (contoh: <i>Star Wars Skywalker</i> dan <i>The Gentlemen</i>) tapi tingkat popularitas tinggi.

>Metascore sendiri dianggap sebagai rating dari movie yang diberikan oleh kelompok kritikus film dunia dan opini mereka dibentuk dalam rupa weighted average score. Tentunya semakin tinggi metascore dan imdb rating nya pasti movie tersebut semakin menarik untuk ditonton. Untuk pengertian lebih mendalam ttg metascore bisa merefer ke __[link ini](https://www.imdb.com/list/ls051211184/)__.

>Lalu, apakah makin banyak yg nge-vote maka makin populer filmnya?\
>Ternyata jumlah voters pun ga menjamin tingkat popularitas, movies seperti <i>The Gentlemen</i> yang jumlah voters kurang lebih 100.000 jika dibandingkan dengan <i>Parasite</i> yg jumlahnya 400.000 an (4x nya) dikatakan populer.

>Pertanyaan besar yg muncul ttg popularitas di tahun 2019 mungkin ini:\
><b>Bagaimana dengan Avengers: Endgame? Mengapa tidak termasuk ke top 7 di list?</b>\
>Avengers: Endgame masih termasuk top 20 menurut tingkat popularitas imdb dengan:
> - imdb rating = 8.4
> - metascore = 78
> - voters = 715.225

>Hmm...beda banget kan sama movie2 yg ada di list top 7...jadi apa cara yg dipakai imdb untuk memeringkat popularitas?

>Dari hasil pencarian di google, saya menemukan seseorang yg telah lama berkecimpung dengan imdb. Teman2 bisa merefer ke __[link ini](https://www.quora.com/What-does-popularity-on-IMDB-mean)__ untuk melihat lebih detil tentang popularitas film di imdb berdasarkan keterangan orang tersebut. Singkatnya nih...film di imdb itu makin populer kalau makin banyak yang klik link di title nya. Jadi dalam case capstone ini, Star Wars Skywalker di peringkat pertama di antara movie2 & film2 lainnya karena title "Star Wars: ... Skywalker" nya banyak yg ngeklik. 

>Sayangnya karena ilmu saya belum banyak, saya belum bisa kumpulin data berapa banyak title nya itu diklik untuk memastikan bener ga si keterangan yang saya baca...\
>Tapi...dengan adanya tabel dan plot yang tersaji sebagai hasil capstone yg telah dibuat, teman2 bisa notice kejanggalan2 yang muncul dari tingkat popularitas yang dibuat sama imdb. Secara simple dari 7 film/movie tersebut bisa terlihat perbedaan peringkatnya kalau kita lihat dari sisi <i><b>peringkat popularitas</b></i> nya (saat masuk ke localhost:5000 bisa refer ke tabel yang ada dibawah plot) dan <i><b>peringkat imdb rating</b></i> nya (bisa refer ke plot nya). Dengan notice adanya kejanggalan tsb kita jadi berpikir lebih jauh, "kenapa bisa gitu ya peringkatnya?"

>Sekian analisis saya, semoga membantu teman2 untuk sama2 merenung dan sama2 belajar lebih dalam lg ttg data analisis :D

Thank you sudah menyempatkan waktu untuk membaca Readme ini :D

Cheers!