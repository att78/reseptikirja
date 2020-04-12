from application import app, db
from flask import redirect, render_template, request, url_for
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm
from flask_login import login_required
from flask_login import current_user
from application.auth.models import User