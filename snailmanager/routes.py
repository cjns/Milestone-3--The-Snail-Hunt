from flask import render_template, request, redirect, url_for
from snailmanager import app, db
from snailmanager.models import User, Observation


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/add_data", methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        # Retrieve form data
        new_observation = Observation(
            observation_date=request.form.get("observation_date"),
            observation_time=request.form.get("observation_time"),
            snail_colour=request.form.get("snail_colour"),
            banding_count=request.form.get("banding_count"),
            observation_count=request.form.get("observation_count"),
            habitat=request.form.get("habitat"),
            location=request.form.get("location"),
            recorder=request.form.get("recorder")
        )
        db.session.add(new_observation)
        db.session.commit()
        return redirect(url_for("data"))
    return render_template("add_data.html")