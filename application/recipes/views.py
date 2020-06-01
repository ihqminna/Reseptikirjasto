from application import app, db
from flask import render_template, request, redirect, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
	return render_template("recipes/lists.html", recipes = Recipe.query.all())

@app.route("/recipes/new/")
def recipes_form():
	return render_template("recipes/new.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
def recipes_create():
	form = RecipeForm(request.form)

	if not form.validate():
		return render_template("recipes/new.html", form = form)

	nimi = form.nimi.data
	annoksia = form.annoksia.data
	aika = form.aika.data
	ohje = form.ohje.data

	r = Recipe(nimi, annoksia, aika, ohje)

	db.session().add(r)
	db.session().commit()

	return redirect(url_for("recipes_index"))
