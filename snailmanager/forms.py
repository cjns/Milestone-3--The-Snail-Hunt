from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
# Adjust the import path based on your app's structure
from snailmanager.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=25,
               message='Username must be between 3 and 25 characters long.')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message='Password must be at least 6 characters long.')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """
        Validate the username by checking if it's already taken in the
        database.

        This function queries the database for the provided username. If a user
        with that username already exists, it raises a ValidationError.

        Parameters:
        username (str): The username to validate.

        Raises:
        ValidationError: If the username is already taken.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'Username is already taken. Please choose a different one.')


# Form Login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=25,
               message='Username must be between 3 and 25 characters long.')
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
