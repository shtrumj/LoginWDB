from flask import Blueprint, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from datetime import datetime
import Website.forms
from Website.forms import SitesForm, sysadmin
from Website.db_model import Sites, sysadmin
from Website import db

view = Blueprint('views', __name__)


@view.route('/addsite', methods=['GET', 'POST'])
def siteadd():
    form = SitesForm()
    if request.method == 'POST':
        siteName = request.form.get('siteName')
        siteAdmin = request.form.get('siteAdmin')
        OWA_URL = request.form.get('OWA_URL')
        FireWall_URL = request.form.get('FireWall_URL')
        siteContact = request.form.get('siteContact')
        siteAddress = request.form.get('siteAddress')
        internalDomain = request.form.get('internalDomain')
        ExternalDomain = request.form.get('ExternalDomain')
        ExternalIPAddress = request.form.get('ExternalIPAddress')
        new_site = Sites(siteName=siteName, siteAdmin=siteAdmin, OWA_URL=OWA_URL, FireWall_URL=FireWall_URL,
                         siteContact=siteContact, siteAddress=siteAddress, internalDomain=internalDomain,
                         ExternalDomain=ExternalDomain,
                         ExternalIPAddress=ExternalIPAddress)
        db.session.add(new_site)
        db.session.commit()

    return render_template('Add-Site.html', form=form)


@view.route('/add-sysadmin', methods=['GET', 'POST'])
def addsysadmin():
    form = Website.forms.sysadmin(request.form)
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastName = request.form.get('lastName')
        dateOfBirth = request.form.get('dateOfBirth')
        phoneNumber = request.form.get('phoneNumber')
        new_sysadmin = sysadmin(firstname=firstname, lastName=lastName, dateOfBirth=dateOfBirth,
                                phoneNumber=phoneNumber)
        db.session.add(new_sysadmin)
        db.session.commit()

    return render_template('addSysAdmin.html', form=form)
