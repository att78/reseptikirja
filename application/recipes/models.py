from application import db
from application.models import Base
from sqlalchemy.sql import text

class Recipe(Base):


    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.Text, nullable=False)

    creator = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)

    #ingredients = db.relationship("IngredientInRecipe", backref="recipe", lazy = 'subquery')                    


    def __init__(self, name, description):
        self.name = name
        self.description=description
        


    @staticmethod
    def find_best_user():
        stmt = text("SELECT COUNT(recipe.id), account.name FROM account"
                     " LEFT JOIN recipe ON recipe.creator = account.id"
                     " GROUP BY account.name"
                     " ORDER BY COUNT(recipe.id) DESC"
                     " LIMIT 1")
                     
        res = db.engine.execute(stmt)

        response = None
        space = " ("
        for row in res:
            response = row[1]+space+str(row[0])+")"
        return response    

