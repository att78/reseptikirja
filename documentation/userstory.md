# Userstoryt

SQL-lauseissa symboli "?" tarkoittaa käyttäjän antamaa parametria.


### Tapaus 1
Käyttäjälta voi kirjautua sisään. 

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.username = ? AND account.password = ?


### Tapaus 2
Käyttäjä voi kirjautua ulos. 

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.id = ?


### Tapaus 3
Käyttäjä voi lisätä raaka-aineita

INSERT INTO ingredient (date_created, date_modified, name, unit, creator) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)


### Tapaus 4
Käyttäjä voi lisätä reseptejä tietokantaan.

INSERT INTO recipe (date_created, date_modified, name, description, creator) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

### Tapaus 5
Käyttäjä voi muokata reseptejä.

UPDATE recipe SET date_modified=CURRENT_TIMESTAMP, description=? WHERE recipe.id = ?


### Tapaus 6

Käyttäjä voi lisätä lempireseptilistaan reseptin. 

INSERT INTO favourites (recipe_id, account_id) VALUES (?, ?)


### Tapaus 7

Käyttäjä voi poistaa reseptejä lempireseptilistasta.

DELETE FROM favourites WHERE favourites.recipe_id = ? AND favourites.account_id = ?


### Tapaus 8

Uusi käyttäjä voi rekisteröityä käyttäjäksi.

INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)


### Tapaus 9

Käyttäjä voi yhdistää raaka-aineita resepteihin.

INSERT INTO ingredient_in_recipe (date_created, date_modified, recipe, ingredient, amount) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)


### Tapaus 10

Käyttäjä näkee lempireseptinsä listattuna main-sivullaan.

SELECT recipe FROM favourites WHERE user.id='?';

SELECT recipe.id AS recipe_id, recipe.date_created AS recipe_date_created, recipe.date_modified AS recipe_date_modified, recipe.name AS recipe_name, recipe.description AS recipe_description, recipe.creator AS recipe_creator, anon_1.account_id AS anon_1_account_id 
FROM (SELECT account.id AS account_id 
FROM account 
WHERE account.id = ?) AS anon_1 JOIN favourites AS favourites_1 ON anon_1.account_id = favourites_1.account_id JOIN recipe ON recipe.id = favourites_1.recipe_id ORDER BY anon_1.account_id


### Tapaus 11

Käyttäjä voi poistaa reseptin.

DELETE FROM recipe WHERE recipe.id = ?


### Tapaus 12

Käyttäjä näkee kaikki reseptit listattuna.
Teoriassa näin: 

SELECT * FROM recipe


Sovelluksessa toiminnassa oleva sql-lause: 

SELECT recipe.id AS recipe_id, recipe.date_created AS recipe_date_created, recipe.date_modified AS recipe_date_modified, recipe.name AS recipe_name, recipe.description AS recipe_description, recipe.creator AS recipe_creator 
FROM recipe


### Tapaus 13

Käyttäjä näkee kaikki raaka-aineet listattuna.

SELECT * FROM INGREDIENTS;


Sovelluksessa toiminnassa oleva sql-lause:

SELECT ingredient.id AS ingredient_id, ingredient.date_created AS ingredient_date_created, ingredient.date_modified AS ingredient_date_modified, ingredient.name AS ingredient_name, ingredient.unit AS ingredient_unit, ingredient.creator AS ingredient_creator 
FROM ingredient



### Tapaus 14

Admin näkee kaikki käyttäjät listattuna

Teoriassa:

SELECT * FROM accounts;

Sovelluksessa:

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account


### Tapaus 15

Admin näkee, ketkä käyttäjät ovat admineja ja ketkä eivät.

SELECT role.id AS role_id, role.date_created AS role_date_created, role.date_modified AS role_date_modified, role.name AS role_name, anon_1.account_id AS anon_1_account_id 
FROM (SELECT account.id AS account_id 
FROM account) AS anon_1 JOIN userroles AS userroles_1 ON anon_1.account_id = userroles_1.account_id JOIN role ON role.id = userroles_1.role_id ORDER BY anon_1.account_id


### Tapaus 16

Admin voi poistaa raaka-aineita

DELETE FROM ingredient WHERE ingredient.id = ?

### Tapaus 17

Eniten reseptejä luonut käyttäjä nimetään reseptilistan yhteydessä:

"SELECT COUNT(recipe.id), account.name FROM account"
                     " LEFT JOIN recipe ON recipe.creator = account.id"
                     " GROUP BY account.name"
                     " ORDER BY COUNT(recipe.id) DESC"
                     " LIMIT 1")


### Tapaus 18

Admin voi päättää voi vaihtaa käyttäjän roolin.

SELECT role.id AS role_id, role.date_created AS role_date_created, role.date_modified AS role_date_modified, role.name AS role_name 
FROM role 
WHERE role.name = ?


### Tapaus 19

Käyttäjä näkee suosituimmat 3 reseptiä

SELECT COUNT(favourites.account_id), recipe.name, recipe.id FROM favourites LEFT JOIN recipe ON recipe.id = favourites.recipe_id GROUP BY recipe.name ORDER BY COUNT(favourites.account_id) DESC LIMIT 3

