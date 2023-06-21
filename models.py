from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Float
import datetime


db = SQLAlchemy()

#from .models import User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    role = db.Column(db.Integer)

    def __init__(self, email, password, name, role):
        self.email=email
        self.password=password
        self.name=name
        self.role=role

#from .models import User
class Meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    num = db.Column(db.String(10))
    units = db.Column(Float(precision=4, asdecimal=True))
    balance = db.Column(db.Numeric(precision=10, scale=2))

    def __init__(self, user_id, num, units, balance):
        self.user_id=user_id
        self.num=num
        self.units=units
        self.balance=balance


class Emergency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(Float(precision=4, asdecimal=True))
    price = db.Column(db.Numeric(precision=10, scale=2))

    def __init__(self, units, price):
        self.units=units
        self.price=price

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    used_units = db.Column(Float(precision=4, asdecimal=True))
    remaining_units = db.Column(Float(precision=4, asdecimal=True))
    activity = db.Column(db.String(30))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())

    def __init__(self, user_id, used_units, remaining_units, activity, created_at):
        self.user_id=user_id
        self.used_units=used_units
        self.remaining_units=remaining_units
        self.activity=activity
        self.created_at=created_at
