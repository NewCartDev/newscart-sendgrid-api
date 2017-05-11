from flask import Flask
import os
from blueprints.templates import TEMPLATE

APP = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'), instance_relative_config=True)

# Load the default configuration
APP.config.from_object('config.default')

# Load the configuration from the instance folder
APP.config.from_pyfile('config.py')

APP.register_blueprint(TEMPLATE, url_prefix='/templates')
