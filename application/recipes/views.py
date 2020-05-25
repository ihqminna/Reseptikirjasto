from application import app
from flask import render_template, request

@app.route("/recipes/new/")
def recipes_form():
	return render_template("recipes/new.html")

@app.route("/recipes/", methods=["POST"])
def recipes_create():
	nimi = request.form.get("nimi")
	annoksia = request.form.get("annoksia")
	aika = request.form.get("aika")
	ohje = request.form.get("ohje")

	r = Recipe(nimi, annoksia, aika, ohje)

	db.session().add(r)
	db.session().commit()

	return "Kiitos reseptistä!"
