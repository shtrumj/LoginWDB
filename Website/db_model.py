import datetime
from flask_wtf.file import FileField, FileRequired, FileAllowed
from . import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, confirmed, admin=False, confirmed_on=None):
        self.username = username
        self.email = email
        self.password = password
        self.confirmed_on = confirmed_on
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.username


class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    siteName = db.Column(db.String(80), unique=True, nullable=False)
    siteAdmin = db.Column(db.String(80), unique=True, nullable=False)
    OWA_URL = db.Column(db.String(80), unique=True, nullable=False)
    FireWall_URL = db.Column(db.String(80), unique=True, nullable=False)
    siteContact = db.Column(db.String(80), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    siteAddress = db.Column(db.DateTime, nullable=False)
    sitePictures = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

    def __init__(self, siteName, siteAdmin, OWA_URL, FireWall_URL, siteContact, registered_on, siteAddress, sitePictures):
        self.siteName = siteName
        self.siteAdmin = siteAdmin
        self.OWA_URL = OWA_URL
        self.FireWall_URL = FireWall_URL
        self.siteContact = siteContact
        self.registered_on = datetime.datetime.now()
        self.siteAddress = siteAddress
        self.sitePictures = sitePictures


