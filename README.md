# reseptikirja

Tarkoitus on luoda reseptikirja, joka pyörii herokussa tai vastaavassa palvelussa. Käyttäjätapaukset/User storyt on käsitelty omassa tiedostossaan. Ohessa linkki siihen: 

[Käyttäjätapauksia](https://github.com/att78/reseptikirja/blob/master/documentation/userstory.md)

Ohessa päivitetty versio arkkitehtuurista: 

![Arkkitehtuuri](https://github.com/att78/reseptikirja/blob/master/documentation/englanniksi%20(1).jpg)


Tietokanta on normalisoitu. Tietokannan luovat sql-lauseet on lueteltu omassa tiedostossaan, johon pääsee alla olevasta linkistä. 

[SQL-lauseet tietokannan luomiseksi](https://github.com/att78/reseptikirja/blob/master/documentation/createtable.md)



 
Sovelluksessä on käytössä testi-käyttäjätunnukset adminille ja tavalliselle käyttäjälle.
Admin:
### Account: testiAdmin
### salasana: testiAdmin 

Peruskäyttäjä:
### Account: testiBasic
### salasana: testiBasic

Samat tunnukset toimivat sekä sovellusta ajettaessa lokaalisti, että herokussa. Sovellukseen voi tehdä halutessaan myös tunnukset ihan itse. Heroku-version tietokannasta löytyy vielä jääminä menneestä käyttäjätunnuksia, jotka eivät täytä validoinnoin ehtoja. Ne on lisätty ennen validointia ja jääneet sinne siksi roikkumaan. Nykyisellään vastaavien luomisen ei pitäisi enää onnistua.

Sovellus löytyy Herokusta. :

[Reseptikirja herokussa](https://reseptikirja2020.herokuapp.com/)

Sovelluksella on alustava käyttöohje: 
[Manuaali](https://github.com/att78/reseptikirja/blob/master/documentation/manual.md)

Harjoitustyön eteneminen on raportoitu erillisessä dokumentissa:

[Viikkoraportit](https://github.com/att78/reseptikirja/blob/master/documentation/weeks.md)


Tsoha-kurssin jälkeiseen maailmaan jää reseptikirjan shoppailulistan rakentaminen. Se on tarkoitus tehdä, sillä tälle harjoitustyölle on olemassa loppukäyttäjä ja haluttuun käyttötapaan liittyy hyvin olennaisesti mahdollisuus tehdä shoppailua varten lista resepteistä. On myös hyvin todennäköistä, että sovelluksen lopullinen sijoituspaikka ei ole Heroku, joten tulevaisuudessa sovellus todennäköisesti täytyy konfiguroida yhteensopivaksi loppukäyttäjän haluaman pilvipalvelun kanssa. Todennäköisesti jossakin kohtaa tulee sovelluksen "face-liftin" aika, mutta tällä hetkellä loppukäyttäjällä ei ole visuaalisesta ilmeestä voimakkaita mielipiteitä.
