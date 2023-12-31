import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager  # Import Flask-Login's LoginManager

# Check and import environment variables if in a development environment
if os.path.exists("env.py"):
    import env  # noqa

# Instantiate Flask application
app = Flask(__name__)

# Application configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the route name of your login view


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    """
    User loader callback for Flask-Login.

    This function is used by Flask-Login to reload the user object from
    the user ID stored in the session. It takes a unicode ID and uses that
    to get the user from the database.

    Parameters:
    user_id (str): The unicode ID of the user to load.

    Returns:
    User: The user object if found, else None.
    """
    # Import inside function to avoid circular imports
    from snailmanager.models import User
    return User.query.get(int(user_id))


from snailmanager import routes  # noqa
