from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# __name__ is predefined variable
# flask uses the location of the module her
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# The bottom import is a workaround to circular imports
from app import routes, models
