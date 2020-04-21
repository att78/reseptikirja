# Userstoryt


### Tapaus 1
Käyttäjälta voi kirjautua sisään. 


### Tapaus 2
Käyttäjä voi kirjautua ulos. 

### Tapaus 3
Käyttäjä voi lisätä raaka-aineita
INSERT INTO Ingredient (name, unit) VALUES ('***','***');

### Tapaus 4
Käyttäjä voi lisätä reseptejä tietokantaan.
INSERT INTO Recipe (name, description) VALUES ('***','***'); 

### Tapaus 5
Käyttäjä voi muokata reseptejä.

### Tapaus 6

Käyttäjä voi lisätä lempireseptilistaan reseptin. 

### Tapaus 7

Käyttäjä voi poistaa reseptejä lempireseptilistasta.


### Tapaus 8

Uusi käyttäjä voi rekisteröityä käyttäjäksi.
INSERT INTO USER (name, username, password) VALUES ('***', '***','***');

### Tapaus 9

Käyttäjä voi yhdistää raaka-aineita resepteihin.

### Tapaus 10

Käyttäjä näkee lempireseptinsä listattuna main-sivullaan.



### Tapaus 11

Käyttäjä voi poistaa reseptin
DELETE FROM RECIPE WHERE recipe.id = '*';

### Tapaus 12

Käyttäjä näkee kaikki reseptit listattuna.

SELECT * FROM RECIPE;

### Tapaus 13

Käyttäjä näkee kaikki raaka-aineet listattuna.

SELECT * FROM INGREDIENTS;

### Tapaus 14

Admin näkee kaikki käyttäjät listattuna

SELECT * FROM accounts;


### Tapaus 15

Admin voi päättää, ketkä käyttäjät ovat admineja ja ketkä eivät.


### Tapaus 16

Admin voi poistaa raaka-aineita

DELETE FROM INGREDIENT where ingredient.id='*';
