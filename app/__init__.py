import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api.views import users
    app.register_blueprint(users.user_route)

    return app    