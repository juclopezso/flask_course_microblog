from flask import Flask

# __name__ is predefined variable
# flask uses the location of the module her
app = Flask(__name__)

# The bottom import is a workaround to circular imports
from app import routes
