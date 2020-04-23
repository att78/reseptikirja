# reseptikirja

Tarkoitus on luoda reseptikirja, joka pyörii herokussa tai vastaavassa palvelussa. Käyttäjätapaukset/User storyt on käsitelty omassa tiedostossaan. Ohessa linkki siihen: 

[Käyttäjätapauksia](https://github.com/att78/reseptikirja/blob/master/documentation/userstory.md)

Ohessa päivitetty versio arkkitehtuurista: 

![Alustava arkkitehtuuri](https://github.com/att78/reseptikirja/blob/master/documentation/viikko5%20update.jpg)

viikko2: tietokantaan voi lisätä reseptin ja reseptiä voi muokata. reseptikirja on viety herokuun ja näyttäisi toimivan siellä.

viikko3: sovellukseen voi rekisteröityä ja kirjautua sekä sisään että ulos. Sovelluksessa voi kirjautuneena käyttäjänä valita reseptin lempireseptiksi tai poistaa lempiresepteistä.

viikko4: sovelluksesssa voi myös poistaa reseptin eli resepteille on nyt täysi crud. Sovelluksessa on otettu bootstrap käyttöön.

viikko5: sovelluksessa voi lisätä, muokata ja poistaa raaka-aineita. Taustalle on tehty koodia raaka-aineiden lisäämiseksi resepteihin, mutta näitä toiminnallisuuksia ei tule käyttäjälle asti vielä tämän viikon päivitykseen. Sovelluksessa on myös otettu käyttöön autorisointi. Ainoastaan admin-oikeuksilla voi poistaa tietokannasta reseptejä ja raaka-aineita sekä antaa muille admin-oikeuksia. Edellämainittu voi kuulostaa paljolta työltä, mutta todellisuudessa laatu on vienyt enemmän aikaa. Tämän viikon aikana reseptikirja on käynyt läpi ison laadullisen päivityksen. Reseptikirjan validointia on paranneltu, html-koodiin on tehty merkittäviä semanttisia parannuksia ja erilaisia bugeja on metsästetty, löydetty ja korjailtu. bugi-parvesta on varmasti vielä karkuunpäässeitäkin vikkeliä yksilöitä. Sen lisäksi käyttöliittymää on muokattu siten, että käyttäminen olisi johdonmukaista ja selkeää.

viikko6: Sovellukseen on lisätty käyttäjän lempireseptien listaus. Käyttäjä näkee omat lempireseptinsä listattuna yhdellä klikkauksella. Armottoman jumppauksen jälkeen reseptit ja raaka-aineet ovat liittyneet nätisti toisiinsa. Ruokaresepteihin voi siis liittää raaka-aineita. Näitä liitoksia voi halutessaan myös muokata ja poistaa. Suuret kokonaisuudet tietokantojen osalta ovat tässä. Viimeiselle viikolle jäi kaikenlaista hiomista, mm. tuon viimeksimainitun suuren kokonaisuuden validointi on vielä "köh köh"-vaiheessa. Validaattorit tehty, mutta käyttöönotto uupuu. Teoriassa se on vain "pari riviä" oikeaan metodiin, mutta jotain ongelmia oli senkin kanssa. Pientä visuaalista hiomista on jo tehty, mutta kokonaisuuden ulkoasun viimeistely jää suurimmaksi osaksi viikolle 7. HTML-semantiikka on pääosin käyty läpi ja melko toimivaksi todettu. Joitakin yksittäisiä ongelmia saattaa vielä olla.
 
Sovelluksessä on käytössä testi-käyttäjätunnukset adminille ja tavalliselle käyttäjälle.
Admin:
### Account: testiAdmin
### salasana: testiAdmin 

Peruskäyttäjä:
### Account: testiBasic
### salasana: testiBasic

Samat tunnukset toimivat sekä sovellusta ajettaessa lokaalisti, että herokussa. Sovellukseen voi tehdä halutessaan myös tunnukset ihan itse. Kannattaa kuitenkin huomata, että rekisteröinnin validointi on vieläkin rajallinen. 

Sovellus löytyy Herokusta. :

[Reseptikirja herokussa](https://reseptikirja2020.herokuapp.com/)


Sovelluksella on alustava käyttöohje: 
[Manuaali](https://github.com/att78/reseptikirja/blob/master/documentation/manual.md)

Tsoha-kurssin jälkeiseen maailmaan jää reseptikirjan shoppailulistan rakentaminen.


