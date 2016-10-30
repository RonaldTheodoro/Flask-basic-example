import os
import sys
from flask import Flask 
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from decouple import config 


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

if not app.config['DEBUG']:
    app.config['SECRET_KEY'] = config('SECRET_KEY')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.users.views import mod as users_module
app.register_blueprint(users_module)
