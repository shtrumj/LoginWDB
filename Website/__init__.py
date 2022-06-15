from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "DB/database.db"
UPLOAD_FOLDER = 'static/uploads/'


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'UPLOAD'
    app.config['SECRET_KEY'] = 'b nhcfje83hdnijnoejrvi9ehdidjnie9'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    db.init_app(app)

    from .view import view
    from .auth import auth
    from .viewer import viewer

    app.register_blueprint(view, url_prefix='/', template_folder='templates')
    app.register_blueprint(viewer, url_prefix='/', template_folder='templates')

    app.register_blueprint(auth, url_prefix='/', template_folder='templates')
    from Website.db_model import Users
    create_db(app)
    return app


def create_db(app):
    if not path.exists('Website/' + DB_NAME):
        db.create_all(app=app)
        print("Database has this been created")