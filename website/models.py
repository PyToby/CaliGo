from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    pfp = db.Column(db.String(300), nullable=True)
    name = db.Column(db.String(100), nullable=True)
    skills = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.String(20))
    pushups = db.Column(db.Integer)
    pullups = db.Column(db.Integer)
    dips = db.Column(db.Integer)
    skills = db.Column(db.JSON)   # list stored as JSON
    goal = db.Column(db.String(20))

    def check_password(self, password):
        if not self.password:
            return False #If user logged in with an auth provider
        return check_password_hash(self.password, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def remove(self):
        db.session.delete(self)

    def get_id(self):           # tell Flask-Login to use user_id
        return str(self.user_id)
    