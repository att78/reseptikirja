from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from application.ingredients.models import Ingredient



class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=2, message="Name is too short")])
    unit = StringField("Ingredient's unit", [validators.Length(min=1, message="Unit is too short")])
    id = 0
    favourite = False

    
    class Meta:
        csrf = False

