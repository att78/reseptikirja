from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipe_editform(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    form = RecipeForm()
    form.name.data = recipe.name
    form.description.data = recipe.description
    form.id = recipe.id

    return render_template("recipes/edit.html", form = form)



@app.route("/recipes/new/")
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())
  
@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipe_update(recipe_id):

    r = Recipe.query.get(recipe_id)
    form = RecipeForm(request.form)

    if not form.validate():
        return render_template("recipes/edit.html/", form = form)

    r.name = form.name.data
    r.description = form.description.data
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/", methods=["POST"])
def recipe_create():

    form = RecipeForm(request.form)
    r = Recipe(form.name.data,form.description.data)
    
    if not form.validate():
        return render_template("recipes/new.html", form = form)
          
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

