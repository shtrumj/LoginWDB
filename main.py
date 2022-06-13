from Website import create_app
from flask import render_template, flash, redirect, url_for
from Website.db_model import Users
from Website.forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
