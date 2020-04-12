from application import db

#ingredientsInRecipes = db.Table('ingredientsInRecipes',
#    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
#    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
#)

class Ingredient(Base):


    name = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.Text, nullable=False)

    
    creator = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)


    def __init__(self, name, unit):
        self.name = name
        self.unit=unit


