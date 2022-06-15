from flask import Blueprint, render_template, request, flash,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from Website.forms import SitesForm
from Website.db_model import Sites
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
                         siteContact=siteContact, siteAddress=siteAddress, internalDomain=internalDomain,ExternalDomain=ExternalDomain,
                         ExternalIPAddress=ExternalIPAddress)
        db.session.add(new_site)
        db.session.commit()

    return render_template('Add-Site.html', form=form)