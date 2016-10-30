import os
from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# Will be used if you need to email information to the site administrators
ADMINS = frozenset([config('ADMINS')])

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Database configuration
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default=default_dburl)
DATABASE_CONNECT_OPTIONS = config('DATABASE_CONNECT_OPTIONS', default={})
SQLALCHEMY_TRACK_MODIFICATIONS = config('DEBUG', default=False, cast=bool)

# Threads configuration
THREADS_PER_PAGE = config('THREADS_PER_PAGE', default=8, cast=int)

# WTF Forms configuration
WTF_CSRF_ENABLED = config('WTF_CSRF_ENABLED', default=True, cast=bool)
WTF_CSRF_SECRET_KEY = config('WTF_CSRF_SECRET_KEY')

# Recaptcha configuration
RECAPTCHA_USE_SSL = config('RECAPTCHA_USE_SSL', default=False, cast=bool) 
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_OPTIONS = {'theme': 'white'}
