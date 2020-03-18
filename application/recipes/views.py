from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipe_editform(recipe_id):

    return render_template("recipes/edit.html", recipe = Recipe.query.get(recipe_id))



@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html")
  
@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipe_update(recipe_id):

    r = Recipe.query.get(recipe_id)
    r.name = request.form.get("name")
    r.description = request.form.get("description")
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/", methods=["POST"])
def recipe_create():
    r = Recipe(request.form.get("name"),request.form.get("description"))
	
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

