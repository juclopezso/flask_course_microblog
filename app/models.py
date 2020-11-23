from datetime import datetime
from app import db

# User has_many Posts

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # relation to Posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # how to print objects of the class
    def __repr__(self):
        return '<User: {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # SQLAlchemy will set the field to the value of calling that function (note that I did not include the () after utcnow, so I'm passing the function itself, and not the result of calling it)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user.id -> Name of the table in db and the field
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post: {}>'.format(self.body)
