# Reseptikirja-manuaali

## Sovelluksen käyttöönotto
Sovelluksen käyttämiseen tarvitaan nettiselain. Sovelluksen käyttämiseen ei tarvitse asentaa mitään käyttäjän koneelle. 
Reseptikirja pyörii heroku-pilvipalvelussa ja käyttämiseen riittää palveluun rekisteröityminen.
Rekisteröitymisessä vaaditaan nimi, käyttäjätunnus ja salasanan kirjaaminen kahteen kertaan. Nimi ja käyttäjätunnus saavat olla samat eli käytännössä halutessaan voi rekisteröityä pelkällä käyttäjätunnuksella. Nimen tulee olla vähintään 2 merkkiä ja maksimissaan 50 merkkiä pitkä. Salasanan tulee olla vähintään 3 merkkiä ja maksimissaan 100 merkkiä pitkä. Rekisteröitymiseen ja sisäänkirjautumiseen ohjataan sivulla, joka toivottaa tervetulleeksi palveluun.

## Käytön perusteet
Reseptikirjaa käytetään yläreunan navigointipalkin avulla. Siellä on näkyvissä ne toiminnot, joita käyttäjä voi autorisaatiostaan riippuen käyttää. Käyttäjällä voi olla joko perus tai admin-tason oikeudet. Oletusarvolla rekisteröityvä käyttäjä saa perustason oikeudet. Käyttäjä voi lisätä ja muokata reseptejä ja raaka-aineita, mutta ainoastaan admin voi poistaa niitä. Käyttäjä voi muokata ainoastaan omia reseptejään mutta admin voi poistaa minkä tahansa reseptin. Allaolevassa kuvauksessa eri toimintakokonaisuuksiin liittyen kannattaa muistaa autorisaation rooli.

## Ruokareseptit
Ruokaresepteihin liittyy mahdollisuus lisätä reseptejä, muokata reseptejä ja poistaa reseptejä. Resepteillä on aina nimi ja kuvaus. Reseptien kuvauksiin voi myös liittää raaka-aineita. Resepteihin liittyviä raaka-aineita voi myös muokata ja poistaa. Käyttäjä voi myös merkitä reseptejä lempiresepteikseen ja poistaa reseptejä lempiresepteistään. Reseptin kuvaus saa olla maksimissaan 10 000 merkkiä pitkä eli pitempikin resepti mahtuu kuvaukseen.

## Raaka-aineet
Käyttäjä voi lisätä, muokata ja poistaa raaka-aineita. Raaka-aineilla on aina nimi ja mittayksikkö. Kullakin raaka-aineella voi olla vain yksi mittayksikkö, mutta käyttäjä voi tallettaa useita samannimisiä raaka-aineita eri mittayksiköillä. Kulinaristin kannalta tämä on järkevä toimintamalli, sillä käytetyt mittayksiköt ovat usein reseptikohtaisia. Reseptikirjaan voi tallentaa lempireseptinsä juuri sellaisena kuin se alkuperäisessä lähteessäkin on.





