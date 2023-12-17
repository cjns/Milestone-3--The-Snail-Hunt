from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, current_user, login_required
from snailmanager import app, db
from snailmanager.forms import RegistrationForm, LoginForm
from snailmanager.models import Survey, User
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import joinedload


@app.route("/")
def home():
    return render_template("home.html")


# Error handlers
# Error handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403


# Error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# Error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('405.html'), 405


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route("/surveys")
def surveys():
    surveys = Survey.query.options(joinedload(
        Survey.user)).order_by(Survey.survey_date).all()
    return render_template("surveys.html", surveys=surveys)


# Add survey
@app.route("/add_survey", methods=["GET", "POST"])
@login_required
def add_survey():
    surveys = list(Survey.query.order_by(Survey.survey_date).all())
    if request.method == "POST":
        # Retrieve form data
        new_survey = Survey(
            user_id=current_user.id,
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
        flash('Survey added successfully.', 'success-toast')
        return redirect(url_for("surveys"))
    return render_template("add_survey.html", surveys=surveys)


# Edit survey
@app.route("/edit_survey/<int:survey_id>", methods=["GET", "POST"])
@login_required
def edit_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    # Ensure user is the owner of the survey
    if survey.user_id != current_user.id:
        flash('You are not authorised to edit this survey.', 'error-toast')
        abort(403)  # HTTP 403 forbidden
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
        flash('Survey updated successfully.', 'success-toast')
        # Redirect to surveys page
        return redirect(url_for('surveys'))
    return render_template("edit_survey.html", survey=survey)


# Delete survey
@app.route("/delete_survey/<int:survey_id>")
@login_required
def delete_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    if survey.user_id != current_user.id:
        flash('You are not authorised to delete this survey.', 'error-toast')
        abort(403)  # HTTP 403 forbidden
    db.session.delete(survey)
    db.session.commit()
    flash('Survey deleted successfully.', 'success-toast')
    return redirect(url_for("surveys"))


# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Welcome back, {}!'.format(user.username), 'success-toast')
            return redirect(next_page or url_for('home'))
        else:
            flash('Login Failed. Check username and password.', 'error-toast')
    return render_template('login.html', title='Log In', form=form)


# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
