
# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa

# os herokua varten
import os

# Herokun tietokantaa käytetään jos ollaan herokussa
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# Muuten käytetään omaa tietokantaa
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recipes.db"
    # Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)


#Käyttäjätietojen konfigurointia ja kirjautuminen

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."
from flask_login import current_user


# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta application/recipes tiedoston models sisältö
from application.recipes import models

from application.recipes import views

# Käyttäjätiedot
from application.auth import models
from application.auth import views

#raaka-aineet
from application.ingredients import models
from application.ingredients import views


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#tuodaan favouritet mukaan
from application.favourites import tables

# Luodaan lopulta tarvittavat tietokantataulut vain kerran
# eli try-and-catchia käyttäen
try: 
    db.create_all()
except:
    pass
