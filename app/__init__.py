from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# __name__ is predefined variable
# flask uses the location of the module her
app = Flask(__name__)
app.config.from_object(Config)

# initialization of extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# show flask-login where is the login view function 
login.login_view = 'login'

# The bottom import is a workaround to circular imports
from app import routes, models
