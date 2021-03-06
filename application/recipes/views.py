from application import app, db, login_manager, login_required
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

from flask_login import current_user
from application.auth.models import User
from application.ingredients.models import IngredientInRecipe, Ingredient

@app.route("/recipes", methods=["GET"])
@login_required
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all(), best_user = Recipe.find_best_user())

@app.route("/recipes/<recipe_id>/show", methods=["GET"])
@login_required
def recipe_show_one(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    form = RecipeForm()
    form.id = recipe.id
    account = User.query.get(current_user.id)
    if recipe in account.favourites:
        form.favourite = True

    # reseptissä olevien raaka-aineiden oliot
    ingredients_in_recipe =IngredientInRecipe.query.filter(IngredientInRecipe.recipe==recipe.id).all()
       
    already_added = []
    for i in ingredients_in_recipe:
        id_number = i.id
        amount = i.amount
        raw =Ingredient.query.get(i.ingredient)
        
        already_added.append({
            'id': id_number,
            'amount': amount,
            'ingredient': raw            
        })




    return render_template("recipes/recipe.html", recipe = recipe, form=form, already_added=already_added, 
    ingredients_in_recipe = ingredients_in_recipe)


@app.route("/recipes/<recipe_id>/", methods=["GET"])
@login_required
def recipe_editform(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    form = RecipeForm()
    form.name.data = recipe.name
    form.description.data = recipe.description
    form.id = recipe.id
    account = User.query.get(current_user.id)
    if recipe in account.favourites:
        form.favourite = True

    return render_template("recipes/edit.html", form = form, recipe = recipe)



@app.route("/recipes/new/")
@login_required
def recipes_form():
    return render_template("recipes/new.html", form = RecipeForm())
  
@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
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
@login_required
def recipe_create():

    form = RecipeForm(request.form)
    r = Recipe(form.name.data,form.description.data)
    r.creator = current_user.id

    if not form.validate():
        return render_template("recipes/new.html", form = form)
          
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/favourite", methods =["POST"])
@login_required
def recipe_add_favourite(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    account = User.query.get(current_user.id)
    account.favourites.append(recipe)
   
    db.session().commit()

    return redirect(url_for("recipe_show_one", recipe_id=recipe_id))

@app.route("/recipes/<recipe_id>/favourite/remove", methods =["POST"])
@login_required
def recipe_remove_favourite(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    account = User.query.get(current_user.id)
    account.favourites.remove(recipe)
    
    db.session().add(account)
    db.session().commit()

    return redirect(url_for("recipe_show_one", recipe_id=recipe_id))


@app.route("/recipes/<recipe_id>/remove", methods = ["POST"])
@login_required(role="Admin")
def recipe_remove(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    # reseptissä olevien raaka-aineiden oliot
    ingredients_in_recipe =IngredientInRecipe.query.filter(IngredientInRecipe.recipe==recipe.id).all()
    #raaka-aineiden tuhoaminen
    for i in ingredients_in_recipe:
        db.session().delete(i)

    db.session().delete(recipe)
    db.session().commit()

    return redirect(url_for("recipes_index"))


@app.route("/recipes/myfavourites", methods=["GET"])
@login_required
def favourites_index():
    account = User.query.get(current_user.id)
    my_favourites = account.favourites    
    return render_template("recipes/favourites.html",  my_favourites = my_favourites)
