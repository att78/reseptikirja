from application import db
from application.favourites.tables import favourites
from application.models import Base


userroles = db.Table('userroles',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

class User(Base):

    __tablename__ = "account"
  
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    favourites = db.relationship("Recipe", secondary = favourites, lazy = 'subquery',
    backref = db.backref('users', lazy = True))

    userroles = db.relationship("Role", secondary = userroles, lazy = 'subquery',
    backref = db.backref('users', lazy = True))


    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return [role.name for role in self.userroles]

    def is_admin(self):
        return  any(role.name == "Admin" for role in self.userroles)

    def set_as_admin(self):        
        role = Role.query.filter(Role.name == "Admin").first()
        if role is None:
            role = Role("Admin")
            db.session().add(role)
        self.userroles.append(role)        

    def remove_from_admin(self):

        for i, role in enumerate(self.userroles):
            if role.name == "Admin":
                del self.userroles[i]
                break
   


class Role(Base):

    __tablename__= "role"

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id    






