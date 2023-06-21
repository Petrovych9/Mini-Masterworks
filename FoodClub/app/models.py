from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(150))
    recipes = db.relationship('Recipe')


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('recipe', lazy=True))  # lazy=True вказує, що завантаження пов'язаних об'єктів буде лінивим, тобто вони будуть завантажуватися лише при зверненні до них.
