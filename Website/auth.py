from flask import Blueprint, render_template, url_for, flash, redirect, request
from Website.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from Website.db_model import Users
auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():  # put application's code here
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='succes')
                return render_template('sites_view.html')
            else:
                flash('there was an error', category='error')
    return render_template('login.html', form=form)


@auth.route('/reg', methods=['GET', 'POST'])
def register():  # put application's code here
    form = RegisterForm()
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form.get('password'), method='sha256')
        username = request.form.get('username')
        password = hashed_password
        email = request.form.get('email')
        new_register = Users(username=username, password=password, email=email, confirmed=False)
        db.session.add(new_register)
        db.session.commit()

        flash("User has been registered successfully")
        return redirect(url_for('auth.login'))

    return render_template('Registration.html', form=form)
