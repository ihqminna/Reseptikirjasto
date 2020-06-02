from application import db
from application.ingredients.models import Ingredient
from application.measures.models import Measure

recipe_ingredient = db.Table('recipe_ingredient', db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True), db.Column('ingredient_name', db.Integer, db.ForeignKey('ingredient.nimi'), primary_key=True), db.Column('measure_name', db.String, db.ForeignKey('measure.nimi')), db.Column('amount', db.Integer))

class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nimi = db.Column(db.String, nullable=False)
	annoksia = db.Column(db.Integer, nullable=False)
	aika = db.Column(db.Integer, nullable=False)
	ohje = db.Column(db.String, nullable=False)
	recipe_ingredient = db.relationship('Recipe_Ingredient', secondary=recipe_ingredient, lazy='subquery', backref=db.backref('ingredients', lazy=True))

	def __init__(self, nimi, annoksia, aika, ohje):
		self.nimi = nimi
		self.annoksia = annoksia
		self.aika = aika
		self.ohje = ohje
