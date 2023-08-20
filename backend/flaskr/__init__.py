import flaskr.models

from flask import Flask
from config import DevelopmentConfig
from flaskr.extensions import db, migrate, api

from flaskr.resources.post import bp as post_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(testing_config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    api.register_blueprint(post_bp, url_prefix="/api")

    return app
