from application import db
from application.ingredients.models import Ingredient
from application.measures.models import Measure

ingredient_recipe = db.Table('ingredient_recipe', db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')), db.Column('ingredient_name', db.Integer, db.ForeignKey('ingredient.nimi'), primary_key=True), db.Column('measure_name', db.String, db.ForeignKey('measure.nimi')))


class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nimi = db.Column(db.String, nullable=False)
	annoksia = db.Column(db.Integer, nullable=False)
	aika = db.Column(db.Integer, nullable=False)
	ohje = db.Column(db.String, nullable=False)

	def __init__(self, nimi, annoksia, aika, ohje):
		self.nimi = nimi
		self.annoksia = annoksia
		self.aika = aika
		self.ohje = ohje
