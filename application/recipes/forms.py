from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import validators
from application.recipes.models import Recipe



class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2)])
    description = TextAreaField("Recipe's description")
    id = 0
    favourite = False

    
    class Meta:
        csrf = False
