from flask import Blueprint, render_template, request, flash,redirect
from . import db
from .db_model import Sites
import sqlite3

viewer = Blueprint('viewer', __name__)


@viewer.route('/site', methods=['GET', 'POST'])
def siteviewer():
        sqliteConnection = sqlite3.connect('Website/DB/database.db')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = "select * from sites;"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        return render_template('sites_view.html', objects=record)
