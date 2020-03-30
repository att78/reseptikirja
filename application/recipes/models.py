from application import db
from application.models import Base

class Recipe(Base):


    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.Text, nullable=False)
    #account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
     #                      nullable=False)


    def __init__(self, name, description):
        self.name = name
        self.description=description
        
         
