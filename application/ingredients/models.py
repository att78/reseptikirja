from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.recipes.models import Recipe



class Ingredient(Base):


    name = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.Text, nullable=False) 
    creator = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)


    def __init__(self, name, unit):
        self.name = name
        self.unit=unit


class IngredientInRecipe(Base):
    recipe = db.Column(db.Integer, db.ForeignKey('recipe.id'),
                            nullable = False)
    ingredient = db.Column(db.Integer, db.ForeignKey('ingredient.id'),
                            nullable = False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, recipe, ingredient, amount):
        self.recipe = recipe
        self.ingredient=ingredient
        self.amount = amount



