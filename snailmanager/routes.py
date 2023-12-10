from flask import render_template, request, redirect, url_for
from snailmanager import app, db
from snailmanager.models import User, Survey


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/surveys")
def surveys():
    surveys = list(Survey.query.order_by(Survey.survey_date).all())
    return render_template("surveys.html", surveys=surveys)


@app.route("/add_survey", methods=["GET", "POST"])
def add_survey():
    if request.method == "POST":
        # Retrieve form data
        new_survey = Survey(
            survey_date=request.form.get("survey_date"),
            survey_time=request.form.get("survey_time"),
            yellow_brown_lipped_snail_0_bands=request.form.get("yellow_brown_lipped_snail_0_bands"),
            pink_brown_lipped_snail_0_bands=request.form.get("pink_brown_lipped_snail_0_bands"),
            brown_brown_lipped_snail_0_bands=request.form.get("brown_brown_lipped_snail_0_bands"),
            yellow_brown_lipped_snail_1_band=request.form.get("yellow_brown_lipped_snail_1_band"),
            pink_brown_lipped_snail_1_band=request.form.get("pink_brown_lipped_snail_1_band"),
            brown_brown_lipped_snail_1_band=request.form.get("brown_brown_lipped_snail_1_band"),
            yellow_brown_lipped_snail_many_bands=request.form.get("yellow_brown_lipped_snail_many_bands"),
            pink_brown_lipped_snail_many_bands=request.form.get("pink_brown_lipped_snail_many_bands"),
            brown_brown_lipped_snail_many_bands=request.form.get("brown_brown_lipped_snail_many_bands"),
            yellow_white_lipped_snail_0_bands=request.form.get("yellow_white_lipped_snail_0_bands"),
            pink_white_lipped_snail_0_bands=request.form.get("pink_white_lipped_snail_0_bands"),
            brown_white_lipped_snail_0_bands=request.form.get("brown_white_lipped_snail_0_bands"),
            yellow_white_lipped_snail_1_band=request.form.get("yellow_white_lipped_snail_1_band"),
            pink_white_lipped_snail_1_band=request.form.get("pink_white_lipped_snail_1_band"),
            brown_white_lipped_snail_1_band=request.form.get("brown_white_lipped_snail_1_band"),
            yellow_white_lipped_snail_many_bands=request.form.get("yellow_white_lipped_snail_many_bands"),
            pink_white_lipped_snail_many_bands=request.form.get("pink_white_lipped_snail_many_bands"),
            brown_white_lipped_snail_many_bands=request.form.get("brown_white_lipped_snail_many_bands"),
            survey_habitat=request.form.get("survey_habitat"),
            survey_location=request.form.get("survey_location"),
            survey_recorder=request.form.get("survey_recorder")
        )
        db.session.add(new_survey)
        db.session.commit()
        return redirect(url_for("surveys"))
    return render_template("add_survey.html")