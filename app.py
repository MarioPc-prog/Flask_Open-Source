from flask import Flask


def create_app():
    # create app object
    app = Flask(__name__)
    return app
