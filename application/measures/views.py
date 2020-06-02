from application import app, db
from flask import render_template, request
from application.measures.models import Measure

@app.route("/measures", methods=["GET"])
def measures_index():
	return render_template("measures/lists.html", measures = Measure.query.all())
