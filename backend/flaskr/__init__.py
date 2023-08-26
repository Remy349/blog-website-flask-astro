import flaskr.models

from flask import Flask, jsonify
from config import DevelopmentConfig
from flaskr.extensions import db, migrate, api, cors, jwt

from flaskr.resources.post import bp as post_bp
from flaskr.resources.user import bp as user_bp
from flaskr.resources.auth import bp as auth_bp


def create_app(testing_config=None):
    app = Flask(__name__)

    if testing_config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(testing_config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "message": "The token has expired.",
                    "error": "Token expired.",
                }
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Request does not contain an access token.",
                    "error": "Authorization required.",
                }
            ),
            401,
        )

    api.register_blueprint(post_bp, url_prefix="/api")
    api.register_blueprint(user_bp, url_prefix="/api")
    api.register_blueprint(auth_bp, url_prefix="/api")

    return app
