# Userstoryt


### Tapaus 1
Käyttäjälta voi kirjautua sisään. 
SELECT id FROM account WHERE username="'", password="'";

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

INSERT INTO favourites (account_id,recipe_id) VALUES('account.id','recipe.id');

### Tapaus 7

Käyttäjä voi poistaa reseptejä lempireseptilistasta.
DELETE FROM favourites WHERE account_id= '*', recipe_id = 'recipe.id';

### Tapaus 8

Uusi käyttäjä voi rekisteröityä käyttäjäksi.

INSERT INTO USER (name, username, password) VALUES ('***', '***','***');

### Tapaus 9

Käyttäjä voi yhdistää raaka-aineita resepteihin.


### Tapaus 10

Käyttäjä näkee lempireseptinsä listattuna main-sivullaan.

SELECT recipe FROM favourites WHERE user.id='*';

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

### Tapaus 17

Eniten reseptejä luonut käyttäjä nimetään reseptilistan yhteydessä:

"SELECT COUNT(recipe.id), account.name FROM account"
                     " LEFT JOIN recipe ON recipe.creator = account.id"
                     " GROUP BY account.name"
                     " ORDER BY COUNT(recipe.id) DESC"
                     " LIMIT 1")
