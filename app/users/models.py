from app import db
from app.users import constants as USER


class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), unique=True)
    email = db.Column('email', db.String(120), unique=True)
    password = db.Column('password', db.String(120))
    role = db.Column('role', db.SmallInteger, default=USER.USER)
    status = db.Column('status', db.SmallInteger, default=USER.NEW)
    
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def get_status(self):
        return USER.STATUS[self.status]

    def get_role(self):
        return USER.ROLE[self.role]
