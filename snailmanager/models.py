from snailmanager import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # schema for the User model
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    surveys = db.relationship('Survey', backref='user',
                              lazy=True, cascade="all, delete-orphan")

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
    return f'<User: {self.username}, ID: {self.id}>'


class Survey(db.Model):
    # schema for the Task model
    __tablename__ = 'survey'
    survey_id = db.Column(db.Integer, primary_key=True)
    survey_date = db.Column(db.Date, unique=False, nullable=False)
    survey_time = db.Column(db.Time, unique=False, nullable=False)
    survey_location = db.Column(db.Text, unique=False, nullable=False)
    survey_habitat = db.Column(db.Text, unique=False, nullable=False)
    survey_recorder = db.Column(db.Text, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
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
        # User ID: {self.id}
        return f"""
            Survey ID: {self.survey_id}
            Survey Date: {self.survey_date}
            Survey Time: {self.survey_time}
            Survey Location: {self.survey_location}
            Survey Habitat: {self.survey_habitat}
            Survey Recorder: {self.survey_recorder}
            Yel Br-Lipped 0 Bands: {self.yellow_brown_lipped_snail_0_bands}
            Pink Br-Lipped 0 Bands: {self.pink_brown_lipped_snail_0_bands}
            Br Br-Lipped 0 Bands: {self.brown_brown_lipped_snail_0_bands}
            Yel Br-Lipped 1 Band: {self.yellow_brown_lipped_snail_1_band}
            Pink Br-Lipped 1 Band: {self.pink_brown_lipped_snail_1_band}
            Br Br-Lipped 1 Band: {self.brown_brown_lipped_snail_1_band}
            Yel Br-Lipped >1 Bands: {self.yellow_brown_lipped_snail_many_bands}
            Pink Br-Lipped >1 Bands: {self.pink_brown_lipped_snail_many_bands}
            Br Br-Lipped >1 Bands: {self.brown_brown_lipped_snail_many_bands}
            Yel Wh-Lipped 0 Bands: {self.yellow_white_lipped_snail_0_bands}
            Pink Wh-Lipped 0 Bands: {self.pink_white_lipped_snail_0_bands}
            Br Wh-Lipped 0 Bands: {self.brown_white_lipped_snail_0_bands}
            Yel Wh-Lipped 1 Band: {self.yellow_white_lipped_snail_1_band}
            Pink Wh-Lipped 1 Band: {self.pink_white_lipped_snail_1_band}
            Br Wh-Lipped 1 Band: {self.brown_white_lipped_snail_1_band}
            Yel Wh-Lipped >1 Bands: {self.yellow_white_lipped_snail_many_bands}
            Pink Wh-Lipped >1 Bands: {self.pink_white_lipped_snail_many_bands}
            Br Wh-Lipped >1 Bands: {self.brown_white_lipped_snail_many_bands}
        """
