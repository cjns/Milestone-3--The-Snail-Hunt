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
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the route name of your login view


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Import inside function to avoid circular imports
    from snailmanager.models import User
    return User.query.get(int(user_id))


from snailmanager import routes  # noqa
