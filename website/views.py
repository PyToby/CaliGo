from flask import Blueprint, render_template, request, redirect, url_for
import logging

view = Blueprint('view', __name__)
logger = logging.getLogger(__name__)

@view.route('/')
def home():
    return render_template("index.html")

@view.route('/app')
def app():
    return render_template("theapp.html")