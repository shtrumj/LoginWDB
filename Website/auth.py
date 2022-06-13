from flask import Blueprint, render_template, url_for, flash, redirect
from Website.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash
from . import db
from Website.db_model import Users
auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route('/reg', methods=['GET', 'POST'])
def register():  # put application's code here
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        username = form.username.data
        password = hashed_password
        email = form.email.data
        new_register = Users(username=username, password=password, email=email)
        db.session.add(new_register)
        db.session.commit()

        flash("User has been registered successfully")
        return redirect(url_for('login'))

    return render_template('Registration.html', form=form)
