import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Set up logging configuration
if not app.debug:
    # Create a file handler object
    file_handler = RotatingFileHandler('flask_app.log', maxBytes=10240, backupCount=10)
    
    # Set the logging level
    file_handler.setLevel(logging.INFO)
    
    # Create a formatter object
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    
    # Set the formatter for the file handler
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the app's logger
    app.logger.addHandler(file_handler)

    # Set the logging level for the app's logger
    app.logger.setLevel(logging.INFO)

    # Log that the application has started
    app.logger.info('Flask application startup')

wsgi_app = app.wsgi_app
app.logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views