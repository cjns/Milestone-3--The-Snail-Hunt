from flask import render_template, request, redirect, url_for
from snailmanager import app, db
from snailmanager.models import Survey  # User


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/surveys")
def surveys():
    surveys = list(Survey.query.order_by(Survey.survey_date).all())
    return render_template("surveys.html", surveys=surveys)


# Add survey
@app.route("/add_survey", methods=["GET", "POST"])
def add_survey():
    surveys = list(Survey.query.order_by(Survey.survey_date).all())
    if request.method == "POST":
        # Retrieve form data
        new_survey = Survey(
            survey_date=request.form.get("survey_date"),
            survey_time=request.form.get("survey_time"),
            survey_location=request.form.get("survey_location"),
            survey_habitat=request.form.get("survey_habitat"),
            survey_recorder=request.form.get("survey_recorder"),
            yellow_brown_lipped_snail_0_bands=request.form.get(
                "yellow_brown_lipped_snail_0_bands"),
            pink_brown_lipped_snail_0_bands=request.form.get(
                "pink_brown_lipped_snail_0_bands"),
            brown_brown_lipped_snail_0_bands=request.form.get(
                "brown_brown_lipped_snail_0_bands"),
            yellow_brown_lipped_snail_1_band=request.form.get(
                "yellow_brown_lipped_snail_1_band"),
            pink_brown_lipped_snail_1_band=request.form.get(
                "pink_brown_lipped_snail_1_band"),
            brown_brown_lipped_snail_1_band=request.form.get(
                "brown_brown_lipped_snail_1_band"),
            yellow_brown_lipped_snail_many_bands=request.form.get(
                "yellow_brown_lipped_snail_many_bands"),
            pink_brown_lipped_snail_many_bands=request.form.get(
                "pink_brown_lipped_snail_many_bands"),
            brown_brown_lipped_snail_many_bands=request.form.get(
                "brown_brown_lipped_snail_many_bands"),
            yellow_white_lipped_snail_0_bands=request.form.get(
                "yellow_white_lipped_snail_0_bands"),
            pink_white_lipped_snail_0_bands=request.form.get(
                "pink_white_lipped_snail_0_bands"),
            brown_white_lipped_snail_0_bands=request.form.get(
                "brown_white_lipped_snail_0_bands"),
            yellow_white_lipped_snail_1_band=request.form.get(
                "yellow_white_lipped_snail_1_band"),
            pink_white_lipped_snail_1_band=request.form.get(
                "pink_white_lipped_snail_1_band"),
            brown_white_lipped_snail_1_band=request.form.get(
                "brown_white_lipped_snail_1_band"),
            yellow_white_lipped_snail_many_bands=request.form.get(
                "yellow_white_lipped_snail_many_bands"),
            pink_white_lipped_snail_many_bands=request.form.get(
                "pink_white_lipped_snail_many_bands"),
            brown_white_lipped_snail_many_bands=request.form.get(
                "brown_white_lipped_snail_many_bands")
        )
        db.session.add(new_survey)
        db.session.commit()
        return redirect(url_for("surveys"))
    return render_template("add_survey.html", surveys=surveys)


# Edit survey
@app.route("/edit_survey/<int:survey_id>", methods=["GET", "POST"])
def edit_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    if request.method == "POST":
        # Retrieve form data
        survey.survey_date = request.form.get("survey_date"),
        survey.survey_time = request.form.get("survey_time"),
        survey.survey_location = request.form.get("survey_location"),
        survey.survey_habitat = request.form.get("survey_habitat"),
        survey.survey_recorder = request.form.get("survey_recorder"),
        survey.yellow_brown_lipped_snail_0_bands = request.form.get(
            "yellow_brown_lipped_snail_0_bands"),
        survey.pink_brown_lipped_snail_0_bands = request.form.get(
            "pink_brown_lipped_snail_0_bands"),
        survey.brown_brown_lipped_snail_0_bands = request.form.get(
            "brown_brown_lipped_snail_0_bands"),
        survey.yellow_brown_lipped_snail_1_band = request.form.get(
            "yellow_brown_lipped_snail_1_band"),
        survey.pink_brown_lipped_snail_1_band = request.form.get(
            "pink_brown_lipped_snail_1_band"),
        survey.brown_brown_lipped_snail_1_band = request.form.get(
            "brown_brown_lipped_snail_1_band"),
        survey.yellow_brown_lipped_snail_many_bands = request.form.get(
            "yellow_brown_lipped_snail_many_bands"),
        survey.pink_brown_lipped_snail_many_bands = request.form.get(
            "pink_brown_lipped_snail_many_bands"),
        survey.brown_brown_lipped_snail_many_bands = request.form.get(
            "brown_brown_lipped_snail_many_bands"),
        survey.yellow_white_lipped_snail_0_bands = request.form.get(
            "yellow_white_lipped_snail_0_bands"),
        survey.pink_white_lipped_snail_0_bands = request.form.get(
            "pink_white_lipped_snail_0_bands"),
        survey.brown_white_lipped_snail_0_bands = request.form.get(
            "brown_white_lipped_snail_0_bands"),
        survey.yellow_white_lipped_snail_1_band = request.form.get(
            "yellow_white_lipped_snail_1_band"),
        survey.pink_white_lipped_snail_1_band = request.form.get(
            "pink_white_lipped_snail_1_band"),
        survey.brown_white_lipped_snail_1_band = request.form.get(
            "brown_white_lipped_snail_1_band"),
        survey.yellow_white_lipped_snail_many_bands = request.form.get(
            "yellow_white_lipped_snail_many_bands"),
        survey.pink_white_lipped_snail_many_bands = request.form.get(
            "pink_white_lipped_snail_many_bands"),
        survey.brown_white_lipped_snail_many_bands = request.form.get(
            "brown_white_lipped_snail_many_bands")
        db.session.commit()
    return render_template("edit_survey.html", survey=survey)


# Delete survey
@app.route("/delete_survey/<int:survey_id>")
def delete_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    db.session.delete(survey)
    db.session.commit()
    return redirect(url_for("surveys"))