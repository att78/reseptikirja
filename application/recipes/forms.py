from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import validators
from application.recipes.models import Recipe



class RecipeForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters long")])
    description = TextAreaField("Recipe's description", [validators.Length(min=20, max=10000, message="Description must be between 20 and 10 000 characters")])
    id = 0
    favourite = False

    
    class Meta:
        csrf = False
