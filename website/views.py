from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, user_logged_in
import logging

view = Blueprint('view', __name__)
logger = logging.getLogger(__name__)

@view.route('/')
def home():
    if current_user.is_anonymous:
        return render_template("index.html")
    return render_template('theapp.html')

@view.route('/app')
@login_required
def app():
    return render_template("theapp.html")