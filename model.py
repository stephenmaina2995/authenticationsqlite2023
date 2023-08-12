#model.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
# from app import db

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    type = db.Column(db.Boolean)
    blocked = db.Column(db.Boolean, default=False)
    activity = db.Column(db.Boolean, default=False)

    def __init__(self,username, email, password, type, blocked, activity):
        # self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.type = type
        self.blocked = blocked
        self.activity = activity

    def confirm_password(self,password):
        return check_password_hash(self.password,password)
    
    def __repr__(self):
        return f'<User:{self.username}'