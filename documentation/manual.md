# Reseptikirja-manuaali

Sovelluksen käyttämiseen tarvitaan nettiselain. Sovelluksen käyttämiseen ei tarvitse asentaa mitään käyttäjän koneelle. 
Reseptikirja pyörii heroku-pilvipalvelussa ja käyttämiseen riittää palveluun rekisteröityminen.
Rekisteröitymisessä vaaditaan nimi, käyttäjätunnus ja salasanan kirjaaminen kahteen kertaan. Nimi ja käyttäjätunnus saavat olla samat eli halutessaan voi rekisteröityä pelkällä käyttäjätunnuksella. Nimen tulee olla vähintään 2 merkkiä ja maksimissaan 50 merkkiä pitkä. Salasanan tulee olla vähintään 3 merkkiä ja maksimissaan 100 merkkiä pitkä.

## Käyttö
Reseptikirjaa käytetään yläreunan navigointipalkin avulla. Siellä on näkyvissä ne toiminnot, joita käyttäjä voi autorisaatiostaan riippuen käyttää. Reseptikirjaan voi lisätä reseptejä, muokata reseptejä ja poistaa reseptejä. Käyttäjä voi myös merkitä reseptejä lempiresepteikseen ja poistaa reseptejä lempiresepteistään. Reseptin kuvaus saa olla maksimissaan 10 000 merkkiä pitkä eli pitempikin resepti mahtuu kuvaukseen.

Käyttäjällä voi olla joko perus tai admin-tason oikeudet. Oletusarvolla rekisteröityvä käyttäjä saa perustason oikeudet. Käyttäjä voi lisätä ja muokata reseptejä ja raaka-aineita, mutta ainoastaan admin voi poistaa niitä.




