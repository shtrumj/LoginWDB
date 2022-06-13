import datetime

from . import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, confirmed, admin=False, confirmed_on=None):
        self.username = username
        self.email = email
        self.password = password
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        self.registered_on = datetime.datetime.now()
        self.admin = admin


    def __repr__(self):
        return '<User %r>' % self.username
