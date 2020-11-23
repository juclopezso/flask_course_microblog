import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Config module
class Config(object):
    # SECRET_KEY used as crypographic key
    # used by wtf extension to protect against cross-site request forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # if env variable not set, configure a sqlite db file named app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # to not signal the application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    