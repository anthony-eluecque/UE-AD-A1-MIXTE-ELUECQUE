from flask import Flask
from .context import bp
from . import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app  