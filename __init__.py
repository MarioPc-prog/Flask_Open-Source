
from flask import Flask
from views import main
import os

global app
debug = True


app = Flask(__name__)

app.register_blueprint(main)

app.config['SECRET_KEY'] = "CS205secretkey"

#Local host

# if __name__ == "__main__":
# 	app.run(debug=debug, host = '127.0.0.1')

# AWS 
if __name__ == "__main__":

	app.run(host='0.0.0.0',port='80')









