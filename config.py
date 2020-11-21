import os

# Config module
class Config(object):
    # SECRET_KEY used as crypographic key
    # used by wtf extension to protect against cross-site request forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'