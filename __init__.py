from flask import Flask
from views import main


debug = True

app = Flask(__name__)
app.register_blueprint(main)


def create_app():

	app.run(debug=debug, host='127.0.0.1')

create_app()
