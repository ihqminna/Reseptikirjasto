from application import db

class Ingredient(db.Model):
	nimi = db.Column(db.String, primary_key=True)

	def __init__(self, nimi):
		self.nimi = nimi

