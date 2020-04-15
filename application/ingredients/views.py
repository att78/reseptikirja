from application import app, db, login_manager, login_required
from flask import redirect, render_template, request, url_for
from application.ingredients.models import Ingredient
from application.ingredients.models import IngredientInRecipe
from application.ingredients.forms import IngredientForm
from application.ingredients.forms import IngredientInRecipeForm
#from flask_login import login_required
from flask_login import current_user
from application.auth.models import User


@app.route("/ingredients", methods=["GET"])
@login_required
def ingredients_index():

    return render_template("ingredients/listraw.html", ingredients = Ingredient.query.all())



@app.route("/ingredients/<ingredient_id>/", methods=["GET"])
@login_required
def ingredient_editform(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    form = IngredientForm()
    form.name.data = ingredient.name
    form.unit.data = ingredient.unit
    form.id = ingredient.id
    #account = User.query.get(current_user.id)
    
    return render_template("ingredients/editraw.html", form = form)


@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/newraw.html", form = IngredientForm())


@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredient_create():

    form = IngredientForm(request.form)
    ingredient = Ingredient(form.name.data,form.unit.data)
    ingredient.creator = current_user.id

    if not form.validate():
        return render_template("ingredients/newraw.html", form = form)
          
    db.session().add(ingredient)
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))


@app.route("/ingredients/<ingredient_id>/", methods=["POST"])
@login_required
def ingredient_update(ingredient_id):

    ingredient = Ingredient.query.get(ingredient_id)
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredient/editraw.html/", form = form)

    
    ingredient.name = form.name.data
    ingredient.unit = form.unit.data
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))



@app.route("/ingredients/<ingredient_id>/remove", methods = ["POST"])
@login_required(role="Admin")
def ingredient_remove(ingredient_id):

    ingredient = Ingredient.query.get(ingredient_id)
    db.session().delete(ingredient)

    db.session().commit()

    return redirect(url_for("ingredients_index"))


# Raaka-aineen lisääminen reseptiin

@app.route("/recipes/addraw", methods=["POST"])
@login_required
def recipe_ingredient_create():

    form = IngredientInRecipeForm(request.form)
    r = IngredientInRecipe(form.recipe.data,form.ingredient.data,form.amount.data)
    #r.creator = current_user.id

    if not form.validate():
        return render_template("recipes/edit.html", form = form)
          
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_update"))

#Raaka-aineen poistaminen reseptistä

@app.route("/recipes/<recipe_id>/remove", methods = ["POST"])
@login_required
def ingredient_in_recipe_remove(recipe_id, ingredient_id, amount):

    ingredient_in_recipe = IngredientInRecipe(recipe_id,ingredient_id, amount)
    db.session().delete(ingredient_in_recipe)
    db.session().commit()

    return redirect(url_for("recipes_update"))


#Reseptissä olevan raaka-aineen muokkaaminen
