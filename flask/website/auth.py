
from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask
from .models import User

from .import db
from flask_bcrypt import Bcrypt, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import session

auth = Blueprint('auth', __name__)

app = Flask(__name__)
bcrypt = Bcrypt(app)

@auth.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                
                # Add this line to store the first name in the session
                session['first_name'] = user.first_name
                
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Login Credentials, try again.', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',  methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters. ', category='error')

        elif len(first_name) < 2:
            flash('Name must be greater than 1 character. ', category='error')

        elif password1 != password2:
            flash('Both passwords must match ', category='error')

        elif len(password1) < 7:
            flash('Password must be at least 7 characters. ', category='error')

        else:
            new_user = User(email=email, first_name=first_name, password=bcrypt.generate_password_hash(password1).decode('utf-8'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)
