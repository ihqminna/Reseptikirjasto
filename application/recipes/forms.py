from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class RecipeForm(FlaskForm):
	nimi = StringField("Reseptin nimi", [validators.Length(min=4, message="Liian lyhyt nimi")])
	aika = IntegerField("Aika (min)", [validators.NumberRange(min=1, max=2880)])
	annoksia = IntegerField ("Annokset", [validators.NumberRange(min=1, max=100)])
	ohje = StringField("Ohje", [validators.Length(min=10)])

	class Meta:
		csrf = False
