from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import TextField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms.validators import Required
from wtforms.validators import EqualTo
from wtforms.validators import Email


class LoginForm(FlaskForm):
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])

class RegisterForm(FlaskForm):
    name = TextField('NickName', [Required()])
    email = TextField('Email address', [Required(), Email()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Repeat Password', [
            Required(), 
            EqualTo('password', message='Passwords must match')
        ]
    )
    accept_tos = BooleanField('I accept the TOS', [Required()])
    recaptcha = RecaptchaField()
    