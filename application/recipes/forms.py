from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import validators
from application.recipes.models import Recipe



class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, message="Name is too short")])
    description = TextAreaField("Recipe's description", [validators.Length(min=20, message="Description is too short")])
    id = 0
    favourite = False

    
    class Meta:
        csrf = False
