from flask import render_template, request, redirect, url_for
from flask_login import login_user 
from flask_login import logout_user
  
from application import app, db, login_manager, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("main"))  


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    


@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    username_already_taken=""

    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm(),username_already_taken = username_already_taken)

    form = RegisterForm(request.form)
   
    if not form.validate():
        return render_template("auth/registerform.html", form = form, username_already_taken =username_already_taken)

    #rekisteröinnissä pitää estää saman usernamen valinta
    suggested_account_name = form.username.data
    checked_account = User.query.filter(User.username==suggested_account_name).first()

    if checked_account != None:
        username_already_taken = "Username is already taken. Please pick another one."
        return render_template("auth/registerform.html", form = form, username_already_taken = username_already_taken)


    account = User(form.name.data, form.username.data, form.password.data)

    if db.session.query(User).count() == 0:
        account.set_as_admin()

    db.session().add(account)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/rights", methods =["GET"])
@login_required
def rights_listing():
    users = User.query.all()
    return render_template("auth/rights.html", users = users)

@app.route("/auth/rights/<user_id>", methods =["POST"])
@login_required(role="Admin")
def set_as_admin(user_id):
    
    account = User.query.get(user_id)
    if(account.is_admin()):
        account.remove_from_admin()
    else:
        account.set_as_admin()

    db.session().commit()       
    users = User.query.all()
    return render_template("auth/rights.html", users = users)

