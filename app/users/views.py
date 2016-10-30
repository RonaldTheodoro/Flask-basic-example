from flask import Blueprint
from flask import request
from flask import render_template
from flask import flash
from flask import g
from flask import session
from flask import redirect
from flask import url_for
from werkzeug import check_password_hash
from werkzeug import generate_password_hash
from app import db
from app.users.forms import RegisterForm
from app.users.forms import LoginForm
from app.users.models import User
from app.users.decorators import requires_login


mod = Blueprint('users', __name__)


@mod.route('/')
@requires_login
def home():
    return render_template('users/profile.html', user=g.user)


@mod.before_request
def before_request():
    """Pull user's profile from the database before every reques are treated"""
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    """Login form"""
    form = LoginForm(request.form)
    
    # Make sure date are valid, but doesn't validate passwordnis right
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
    
        # We use werzeug to validade user's password
        if user and check_password_hash(user.password, form.password.data):
            # The session can't be modified as it's signed,
            # it's a safe place to store the user id
            session['user_id'] = user.id
            flash('Welcome {}'.format(user.name))
            return redirect(url_for('users.home'))
        
        flash('Wrong email or password', 'error-message')

    return render_template('users/login.html', form=form)


@mod.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        # Create an user instance not yet stored in the database
        user = User(
            name=form.name.data, 
            email=form.email.data, 
            password=generate_password_hash(form.password.data)
        )
        # Insert the record in our database and commit it
        db.session.add(user)
        db.session.commit()
        # Log the user in, as he now has an id
        session['user_id'] = user.id
        # Flash will display a message to the user
        flash('Thanks for registering')
        # Redirect user to the 'home' method of the user module
        return redirect(url_for('users.home'))
    
    return render_template('users/register.html', form=form)
