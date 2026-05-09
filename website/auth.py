from flask import Blueprint, render_template, request, redirect, url_for
import logging
from .models import User, db
from flask_login import login_user, logout_user, login_required, current_user

logger = logging.getLogger(__name__)

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('signupemail')
        password1 = request.form.get('signuppassword1')
        #password2 = request.form.get('signuppassword2')
        name = email.split("@")[0]

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('signup.html', error='An account with this email already exists.')

        '''if password1 != password2:
            return render_template('signup.html', error='Passwords do not match.')'''

        new_user = User(email=email, name=name)
        new_user.set_password(password1)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template("theapp.html")
        except Exception as e:
            db.session.rollback()
            logger.error(f"Signup error: {e}")
            return render_template('signup.html', error='An error occurred. Please try again later.')
    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('loginemail')
        password = request.form.get('loginpassword')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('view.home'))
        else:
            return render_template('login.html', error="Invalid email or password")
    return render_template('login.html')

@auth.route('/survey')
def survey():
    return render_template("survey.html")