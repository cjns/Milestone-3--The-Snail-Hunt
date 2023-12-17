from snailmanager import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # schema for the User model
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    survey = db.relationship('Survey', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'<User: {self.username}>'


class Survey(db.Model):
    # schema for the Task model
    survey_id = db.Column(db.Integer, primary_key=True)
    survey_date = db.Column(db.Date, unique=False, nullable=False)
    survey_time = db.Column(db.Time, unique=False, nullable=False)
    survey_location = db.Column(db.Text, unique=False, nullable=False)
    survey_habitat = db.Column(db.Text, unique=False, nullable=False)
    survey_recorder = db.Column(db.Text, unique=False, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"), nullable=False)
    yellow_brown_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_brown_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_brown_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    yellow_brown_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_brown_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_brown_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    yellow_brown_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_brown_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_brown_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    yellow_white_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_white_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_white_lipped_snail_0_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    yellow_white_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_white_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_white_lipped_snail_1_band = db.Column(
        db.Integer, unique=False, nullable=False)
    yellow_white_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    pink_white_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)
    brown_white_lipped_snail_many_bands = db.Column(
        db.Integer, unique=False, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # User ID: {self.user_id}
        return f"""
            Survey ID: {self.survey_id}
            Survey Date: {self.survey_date}
            Survey Time: {self.survey_time}
            Survey Location: {self.survey_location}
            Survey Habitat: {self.survey_habitat}
            Survey Recorder: {self.survey_recorder}
            Yellow, Brown Lipped Snail, 0 Bands: {self.yellow_brown_lipped_snail_0_bands}
            Pink, Brown Lipped Snail, 0 Bands: {self.pink_brown_lipped_snail_0_bands}
            Brown, Brown Lipped Snail, 0 Bands: {self.brown_brown_lipped_snail_0_bands}
            Yellow, Brown Lipped Snail, 1 Band: {self.yellow_brown_lipped_snail_1_band}
            Pink, Brown Lipped Snail, 1 Band: {self.pink_brown_lipped_snail_1_band}
            Brown, Brown Lipped Snail, 1 Band: {self.brown_brown_lipped_snail_1_band}
            Yellow, Brown Lipped Snail, Many Bands: {self.yellow_brown_lipped_snail_many_bands}
            Pink, Brown Lipped Snail, Many Bands: {self.pink_brown_lipped_snail_many_bands}
            Brown, Brown Lipped Snail, Many Bands: {self.brown_brown_lipped_snail_many_bands}
            Yellow, White Lipped Snail, 0 Bands: {self.yellow_white_lipped_snail_0_bands}
            Pink, White Lipped Snail, 0 Bands: {self.pink_white_lipped_snail_0_bands}
            Brown, White Lipped Snail, 0 Bands: {self.brown_white_lipped_snail_0_bands}
            Yellow, White, Lipped Snail, 1 Band: {self.yellow_white_lipped_snail_1_band}
            Pink, White Lipped Snail, 1 Band: {self.pink_white_lipped_snail_1_band}
            Brown, White Lipped Snail, 1 Band: {self.brown_white_lipped_snail_1_band}
            Yellow, White Lipped Snail, Many Bands: {self.yellow_white_lipped_snail_many_bands}
            Pink, White Lipped Snail, Many Bands: {self.pink_white_lipped_snail_many_bands}
            Brown, White Lipped Snail, Many Bands: {self.brown_white_lipped_snail_many_bands}
        """
