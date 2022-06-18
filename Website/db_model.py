from datetime import datetime
from datetime import timedelta
from flask_wtf.file import FileField, FileRequired, FileAllowed
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import  func
from . import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow())
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, confirmed, admin=False, confirmed_on=None):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.username


class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    siteName = db.Column(db.String(80), nullable=False)
    siteAdmin = db.Column(db.String(80),nullable=False)
    OWA_URL = db.Column(db.String(80), nullable=False)
    FireWall_URL = db.Column(db.String(80), nullable=False)
    siteContact = db.Column(db.String(80), nullable=False)
    siteAddress = db.Column(db.String(80), nullable=False)
    internalDomain = db.Column(db.String(20))
    ExternalDomain = db.Column(db.String(20))
    ExternalIPAddress = db.Column(db.String(30))

    def __init__(self, siteName, siteAdmin, OWA_URL, FireWall_URL, siteContact, siteAddress, internalDomain, ExternalDomain, ExternalIPAddress):
        self.siteName = siteName
        self.siteAdmin = siteAdmin
        self.OWA_URL = OWA_URL
        self.FireWall_URL = FireWall_URL
        self.siteContact = siteContact
        self.siteAddress = siteAddress
        self.internalDomain = internalDomain
        self.ExternalDomain = ExternalDomain
        self.ExternalIPAddress = ExternalIPAddress


