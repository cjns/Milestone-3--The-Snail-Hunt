from snailmanager import db


class User(db.Model):
    # schema for the User model
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=False, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    observation = db.relationship("Observation", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"""
            User ID: {self.user_id}
            Username: {self.username}
            Email: {self.email}
            Password: {self.password }
        """


class Observation(db.Model):
    # schema for the Task model
    observation_id = db.Column(db.Integer, primary_key=True)
    observation_date = db.Column(db.Date, unique=False, nullable=False)
    observation_time = db.Column(db.Time, unique=False, nullable=False)
    snail_colour = db.Column(db.String(25), unique=False, nullable=False)
    banding_count = db.Column(db.Integer, unique=False, nullable=False)
    location = db.Column(db.Text, unique=False, nullable=False)
    observation_count = db.Column(db.Integer, unique=False, nullable=False)
    recorder = db.Column(db.Text, unique=False, nullable=False)
    habitat = db.Column(db.Text, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id, ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"""
            Observation ID: {self.observation_id}
            Observation Date: {self.observation_date}
            Snail Color: {self.snail_color}
            Banding Counter: {self.banding_count}
            Location: {self.location}
            Habitat: {self.habitat}
            User ID: {self.user_id}
        """
