from application import app, db
from flask import render_template, request
from application.ingredients.models import Ingredient

@app.route("/ingredients", methods=["GET"])
def recipes_index():
	return render_template("ingredients/lists.html", ingredients = Ingredient.query.all())
