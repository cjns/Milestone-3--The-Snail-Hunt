from flask import render_template
from snailmanager import app, db
from snailmanager.models import User, Snails


@app.route("/")
def home():
    return render_template("base.html")