"""
The flask application package.
"""
import logging
from flask import Flask
from flask.logging import create_logger
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
