from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from application.ingredients.models import Ingredient



class IngredientForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters long")])
    unit = StringField("Ingredient's unit", [validators.Length(min=1, max=10, message="Unit must be between 1 and 10 characters long")])
    id = 0
    favourite = False
    
    class Meta:
        csrf = False

