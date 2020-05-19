from application import db

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
