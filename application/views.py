from flask import render_template
from application import app,  login_required
from application.recipes.models import Recipe

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
@login_required
def main():
    
    return render_template("main.html", best_recipes = Recipe.find_best_recipes())


