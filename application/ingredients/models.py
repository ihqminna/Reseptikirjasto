from application import db
from application.measures.models import Measure

class Ingredient(db.Model):
	nimi = db.Column(db.String, primary_key=True)

	#recipes = db.relationship('Recipe', secondary=ingredient_recipe, backref='recipes', lazy='dynamic')

	def __init__(self, nimi):
		self.nimi = nimi

