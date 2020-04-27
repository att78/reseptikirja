from application import db
from application.models import Base
from sqlalchemy.sql import text

class Recipe(Base):


    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.Text, nullable=False)

    creator = db.Column(db.Integer, db.ForeignKey('account.id'),
                          nullable=False)

                       


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



    @staticmethod
    def find_best_recipes():
        stmt = text("SELECT COUNT(favourites.account_id), recipe.name, recipe.id FROM favourites"
                    " LEFT JOIN recipe ON recipe.id = favourites.recipe_id"
                    " GROUP BY recipe.name"
                    " ORDER BY COUNT(favourites.account_id) DESC"
                    " LIMIT 3")

        res = db.engine.execute(stmt)

        best_recipes = []
        for recipe in res:
            id_number = recipe[2]
            name = recipe[1]
            count = recipe[0]
       
            best_recipes.append({
                'id': id_number,
                'name': name,
                'count': count            
            })

        return best_recipes                    