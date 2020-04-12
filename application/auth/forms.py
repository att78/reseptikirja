from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters long")])
    password = PasswordField("Password", [validators.Length(min=3, max=100, message="Password must be between 3 and 100 characters long")])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters long")])
    username = StringField("Username", [validators.Length(min=2, max=50, message="Name must be between 2 and 50 characters long")])
    password = PasswordField("Password", [validators.Length(min=3, max=100, message="Password must be between 3 and 100 characters long")])
    password2 = PasswordField("Password2", [validators.EqualTo("password", message="Passwords do not match")])

    class Meta:
        csrf = False        

