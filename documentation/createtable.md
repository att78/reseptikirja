# Tietokannan "create table"-lauseet on lueteltu alla


CREATE TABLE account (

	id INTEGER NOT NULL, 

	date_created DATETIME,
	
	date_modified DATETIME,
	
	name VARCHAR(144) NOT NULL, 
	
	username VARCHAR(144) NOT NULL, 
	
	password VARCHAR(144) NOT NULL, 
	
	PRIMARY KEY (id)
	
)


CREATE TABLE role (

	id INTEGER NOT NULL, 
	
	date_created DATETIME,
	
	date_modified DATETIME,
	
	name VARCHAR(144) NOT NULL,
	
	PRIMARY KEY (id)
	
)


CREATE TABLE userroles (

	role_id INTEGER NOT NULL, 
	
	account_id INTEGER NOT NULL, 
	
	PRIMARY KEY (role_id, account_id), 
	
	FOREIGN KEY(role_id) REFERENCES role (id), 
	
	FOREIGN KEY(account_id) REFERENCES account (id)
	
)


CREATE TABLE recipe (

	id INTEGER NOT NULL, 
	
	date_created DATETIME, 
	
	date_modified DATETIME, 
	
	name VARCHAR(144) NOT NULL, 
	
	description TEXT NOT NULL, 
	
	creator INTEGER NOT NULL, 
	
	PRIMARY KEY (id), 
	
	FOREIGN KEY(creator) REFERENCES account (id)
	
)


CREATE TABLE ingredient (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	unit TEXT NOT NULL, 
	creator INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(creator) REFERENCES account (id)
)


CREATE TABLE favourites (
	recipe_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (recipe_id, account_id), 
	FOREIGN KEY(recipe_id) REFERENCES recipe (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)


CREATE TABLE ingredient_in_recipe (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	recipe INTEGER NOT NULL, 
	ingredient INTEGER NOT NULL, 
	amount INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe) REFERENCES recipe (id), 
	FOREIGN KEY(ingredient) REFERENCES ingredient (id)
)
