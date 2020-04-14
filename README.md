# reseptikirja

Tarkoitus on luoda reseptikirja, joka pyörii herokussa tai vastaavassa palvelussa. Käyttäjätapaukset/User storyt on käsitelty omassa tiedostossaan. Ohessa linkki siihen: 

[Käyttäjätapauksia](https://github.com/att78/reseptikirja/blob/master/documentation/userstory.md)

Ohessa päivitetty versio arkkitehtuurista: 

![Alustava arkkitehtuuri](https://github.com/att78/reseptikirja/blob/master/documentation/viikko5%20update.jpg)

viikko2: tietokantaan voi lisätä reseptin ja reseptiä voi muokata. reseptikirja on viety herokuun ja näyttäisi toimivan siellä.

viikko3: sovellukseen voi rekisteröityä ja kirjautua sekä sisään että ulos. Sovelluksessa voi kirjautuneena käyttäjänä valita reseptin lempireseptiksi tai poistaa lempiresepteistä.

viikko4: sovelluksesssa voi myös poistaa reseptin eli resepteille on nyt täysi crud. Sovelluksessa on otettu bootstrap käyttöön. 

Sovelluksessä on käytössä testi-käyttäjätunnukset. 

### Account: testi
### salasana: testi 

Samat tunnukset toimivat sekä sovellusta ajettaessa lokaalisti, että herokussa. Sovellukseen voi tehdä halutessaan myös tunnukset ihan itse. Kannattaa kuitenkin huomioida, että käyttäjätunnusten rekisteröinnissä tai kirjautumisessa ei ole validointia eli tämän saattaa saada rikki hyvin helposti. 

Sovellus löytyy Herokusta. :

[Reseptikirja herokussa](https://reseptikirja2020.herokuapp.com/)

Jos aikaa jää, mahdollisesti yritän vielä tehdä shoppailutoiminnon reseptikirjaan.





