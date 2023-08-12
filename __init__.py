import os

from flask import Flask

# from model import *
from main2 import app

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")

    db.init_app(app)
    app.register_blueprint(app)
    return app