from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, message="Name is too short")])
    password = PasswordField("Password", [validators.Length(min=3, message="Password is too short")])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, message="Name is too short")])
    username = StringField("Username", [validators.Length(min=2, message="Name is too short")])
    password = PasswordField("Password", [validators.Length(min=3, message="Password is too short")])
    password2 = PasswordField("Password2", [validators.EqualTo("password", message="Passwords do not match")])

    class Meta:
        csrf = False        

