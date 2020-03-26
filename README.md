# reseptikirja

Tarkoitus on luoda reseptikirja, joka pyörii herokussa tai vastaavassa palvelussa. Käyttäjätapaukset/User storyt on käsitelty omassa tiedostossaan. Ohessa linkki siihen: 

![Käyttäjätapauksia](https://github.com/att78/reseptikirja/blob/master/documentation/userstory.md)

Ohessa päivitetty versio arkkitehtuurista: 

![Päivitetty versio arkkitehtuurista](https://github.com/att78/reseptikirja/blob/master/documentation/updated.jpg)

viikko2: tietokantaan voi lisätä reseptin ja reseptiä voi muokata. reseptikirja on viety herokuun ja näyttäisi toimivan siellä.
viikko3: sovellukseen voi rekisteröityä ja kirjautua sekä sisään että ulos. Sovelluksessa voi kirjautuneena käyttäjänä valita reseptin lempireseptiksi tai poistaa lempiresepteistä.

Sovelluksessä on käytössä testi-käyttäjätunnukset. 

### Account: testi
### salasana: testi 

Samat tunnukset toimivat sekä sovellusta ajettaessa lokaalisti, että herokussa. Sovellukseen voi tehdä halutessaan myös tunnukset ihan itse. Kannattaa kuitenkin huomkoida, että käyttäjätunnusten rekisteröinnissä tai kirjautumisessa ei ole validointia eli tämän saattaa saada rikki hyvin helposti. 

Sovellus löytyy Herokusta. :

[Reseptikirja herokussa](https://reseptikirja2020.herokuapp.com/)



Jos aikaa jää, alla olevassa arkkitehtuurikuvauksessa on idea siitä, mihin sitä ylimääräistä aikaa käytetään:

![Alustava arkkitehtuurikuvaus](https://github.com/att78/reseptikirja/blob/master/documentation/Arkkitehtuurikuvaus.md)





