from flask import Flask
from flask_potion import Api
import os

from potion_test.db import init_db
from potion_test.api import AlphaResource, BetaResource


def create_app():
    """
    Flask app factory method
    """
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASS = os.environ.get('DB_PASS', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME', 'potion_test')
    SECRET_KEY = os.environ.get('SECRET_KEY', '123456')
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['DEBUG'] = os.environ.get('DEBUG') is not None
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:%s/%s' % (
        DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
    return app


def init_app(app):
    """
    Configuring the Flask app's extensions
    """
    # initialize Flask extensions
    app.db = init_db(app)

    # setup Flask-Potion routes
    v1_api = Api(app)
    v1_api.add_resource(BetaResource)
    v1_api.add_resource(AlphaResource)

    return app
