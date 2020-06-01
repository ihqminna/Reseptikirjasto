from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class RecipeForm(FlaskForm):
	nimi = StringField("Reseptin nimi")
	aika = IntegerField("Aika (min)")
	annoksia = IntegerField ("Annokset")
	ohje = StringField("Ohje")

	class Meta:
		csrf = False
