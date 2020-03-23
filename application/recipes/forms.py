from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from application.recipes.models import Recipe



class RecipeForm(FlaskForm):
    name = StringField("Recipe name")
    description = TextAreaField("Recipe's description")
    id = 0

    
    class Meta:
        csrf = False
