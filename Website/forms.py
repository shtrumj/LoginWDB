from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired()], render_kw={'autofocus': True})
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()], render_kw={'autofocus': True})
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('password2', validators=[DataRequired()])
    is_active = BooleanField(label="UserActivation")
    submit = SubmitField('Register')


class SitesForm(FlaskForm):
    siteName = StringField('Site Name', validators=[DataRequired()], render_kw={'autofocus': True})
    siteAdmin = StringField('Site SysAdmin', validators=[DataRequired()])
    OWA_URL = StringField('OWA URL', validators=[DataRequired()])
    FireWall_URL = StringField('Firewall URL', validators=[DataRequired()])
    siteContact = StringField('siteContact', validators=[DataRequired()])
    siteAddress = StringField('Site Address', validators=[DataRequired()])
    internalDomain = StringField('internal domain')
    ExternalDomain = StringField('External Domain')
    ExternalIPAddress = StringField('ExternalIPAddress')
