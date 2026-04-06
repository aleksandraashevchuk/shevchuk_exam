from flask import Flask
from .config import Config
from .db import db
from .routes import api
from .init_db import init_db


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(api)

    with app.app_context():
        init_db()

    return app
