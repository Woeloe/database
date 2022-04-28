from . import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    resident1 = db.Column(db.String(150), nullable=True)
    resident2 = db.Column(db.String(150), nullable=True)
    resident3 = db.Column(db.String(150), nullable=True)
