from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "DB/database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'b nhcfje83hdnijnoejrvi9ehdidjnie9'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .view import view
    from .auth import auth

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from Website.db_model import Users
    create_db(app)
    return app


def create_db(app):
    if not path.exists('Website/' + DB_NAME):
        db.create_all(app=app)
        print("Database has this been created")