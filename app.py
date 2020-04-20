from flask import Flask
def create_app():
    # create app object
    app = Flask(__name__)
    # register the Blueprint by importing and registering 
    from views import main
    app.register_blueprint(main)
    return app
