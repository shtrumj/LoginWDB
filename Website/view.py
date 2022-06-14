from flask import Blueprint, render_template, request
from Website.forms import SitesForm
from Website.db_model import Sites
from Website import db
from flask_uploads import configure_uploads, IMAGES, UploadSet
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
view = Blueprint('views', __name__)

images = UploadSet('images', IMAGES)


@view.route('/sitesview', methods=['GET', 'POST'])
def siteview():
    return render_template('sites_view.html')


@view.route('/addsite', methods=['GET', 'POST'])
def siteadd():
    form = SitesForm()
    if request.method == 'POST':
        siteName = request.form.get('siteName')
        siteAdmin = request.form.get('siteAdmin')
        OWA_URL = request.form.get('siteOWA_URL')
        FireWall_URL = request.form.get('FireWall_URL')
        siteContact = request.form.get('siteContact')
        siteAddress = request.form.get('siteAddress')
        new_site = Sites(siteName=siteName, siteAdmin=siteAdmin, OWA_URL=OWA_URL, FireWall_URL=FireWall_URL, siteContact=siteContact, siteAddress=siteAddress)
        db.session.add(new_site)
        db.session.commit()

    return render_template('Add-Site.html', form=form)