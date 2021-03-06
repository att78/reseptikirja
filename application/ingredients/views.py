from application import app, db, login_manager, login_required
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.ingredients.models import Ingredient
from application.ingredients.models import IngredientInRecipe
from application.ingredients.forms import IngredientForm
from application.ingredients.forms import IngredientInRecipeForm

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
    
    return render_template("ingredients/editraw.html", form = form)


@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/newraw.html", form = IngredientForm())


@app.route("/ingredients/", methods=["POST"])
@login_required(role="Admin")
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
@login_required(role="Admin")
def ingredient_update(ingredient_id):

    ingredient = Ingredient.query.get(ingredient_id)
    form = IngredientForm(request.form)

    if not form.validate():
        return render_template("ingredients/editraw.html/", form = form)

    
    ingredient.name = form.name.data
    ingredient.unit = form.unit.data
    db.session().commit()
  
    return redirect(url_for("ingredients_index"))



@app.route("/ingredients/<ingredient_id>/remove", methods = ["POST"])
@login_required(role="Admin")
def ingredient_remove(ingredient_id):

    ingredient = Ingredient.query.get(ingredient_id)
    #Linkkitaulusta poistaminen, TARKISTA TOIMIVUUS VIELÄ
    ingredient_in_recipes =IngredientInRecipe.query.filter(IngredientInRecipe.ingredient==ingredient.id).all()
    #linkkitaulun kytkösten tuhoaminen
    for i in ingredient_in_recipes:
        db.session().delete(i)

    db.session().delete(ingredient)

    db.session().commit()

    return redirect(url_for("ingredients_index"))



# Raaka-aineen lisääminen reseptiin

@app.route("/recipes/<recipe_id>/addraw", methods=["POST"])
@login_required
def recipe_ingredient_create(recipe_id):

    form = IngredientInRecipeForm(request.form)
    ingredient_id = form.ingredient.data   
    amount = form.amount.data
    r = IngredientInRecipe(recipe_id,ingredient_id,amount)
          
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("recipe_set_ingredients", recipe_id=recipe_id))

#Raaka-aineen poistaminen reseptistä

@app.route("/recipes/<recipe_id>/<ingredient_in_recipe_id>/remove", methods = ["POST"])
@login_required
def recipe_ingredient_remove(ingredient_in_recipe_id,recipe_id):

    ingredient_in_recipe = IngredientInRecipe.query.get(ingredient_in_recipe_id)
    recipe = Recipe.query.get(recipe_id)

    db.session().delete(ingredient_in_recipe)
    db.session().commit()

    return redirect(url_for("recipe_set_ingredients", recipe_id= recipe_id))


# Reseptin tarkastelu raaka-aineen lisäämistä varten

@app.route("/recipes/<recipe_id>/setingredients", methods=["GET"])
@login_required
def recipe_set_ingredients(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    ingredients = Ingredient.query.all()
    form = IngredientInRecipeForm
    # reseptissä olevien raaka-aineiden oliot
    ingredients_in_recipe =IngredientInRecipe.query.filter(IngredientInRecipe.recipe==recipe.id).all()
    
    #listaus ei ole callable, mutta toimii, jos vie tuollaista lennosta rakennettua oliota eteenpäin
    already_added = []
    for i in ingredients_in_recipe:
        id_number = i.id
        amount = i.amount
        raw =Ingredient.query.get(i.ingredient)
    #Huomio itselle: pythonin lentävä olio-hässäkkä. Eli python sallii olioiden luomisen lennosta ilman, että oliolle on luotu muualla luokkaa.     
        already_added.append({
            'id': id_number,
            'amount': amount,
            'ingredient': raw            
        })

   
    return render_template("recipes/addingredients.html", recipe = recipe, ingredients = ingredients, 
    ingredients_in_recipe = ingredients_in_recipe, already_added= already_added, form=form)