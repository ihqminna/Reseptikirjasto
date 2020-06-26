from application import db
from application.ingredients.models import Ingredient
from application.ingredient_recipe.models import Ingredient_recipe

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nimi = db.Column(db.String, nullable=False)
	annoksia = db.Column(db.Integer, nullable=False)
	aika = db.Column(db.Integer, nullable=False)
	ohje = db.Column(db.String, nullable=False)

	#ingredients = db.relationship('Ingredient', secondary=ingredient_recipe, backref='recipes', lazy='dynamic')

	def __init__(self, nimi, annoksia, aika, ohje):
		self.nimi = nimi
		self.annoksia = annoksia
		self.aika = aika
		self.ohje = ohje
