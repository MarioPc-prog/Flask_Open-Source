from flask import Flask
from views import main
import os

global app
debug = True


app = Flask(__name__)

app.register_blueprint(main)

# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# def create_app():

# 	app.run(debug=debug, host='0.0.0.0:80')

# create_app()

# For local host running only - otherwise comment out 
# def create_app():

# 	app.run(debug=debug, host='127.0.0.1')

# create_app()

if __name__ == "__main__":
	app.run(debug=debug, host = '127.0.0.1')








