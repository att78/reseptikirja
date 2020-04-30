# reseptikirja

Tarkoitus on luoda reseptikirja, joka pyörii herokussa tai vastaavassa palvelussa. Käyttäjätapaukset/User storyt on käsitelty omassa tiedostossaan. Ohessa linkki siihen: 

[Käyttäjätapauksia](https://github.com/att78/reseptikirja/blob/master/documentation/userstory.md)

Ohessa päivitetty versio arkkitehtuurista: 

![Arkkitehtuuri](https://github.com/att78/reseptikirja/blob/master/documentation/englanniksi.jpg)


Tietokanta on normalisoitu. Tietokannan luovat sql-lauseet on lueteltu omassa tiedostossaan, johon pääsee alla olevasta linkistä. 

[SQL-lauseet tietokannan luomiseksi](https://github.com/att78/reseptikirja/blob/master/documentation/createtable.md)



 
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

Harjoitustyön eteneminen on raportoitu erillisessä dokumentissa

[Viikkoraportit](https://github.com/att78/reseptikirja/blob/master/documentation/weeks.md)


