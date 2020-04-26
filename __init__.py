from flask import Flask
from views import main



debug = False

app = Flask(__name__)
app.register_blueprint(main)

app.config['SECRET_KEY'] = "CS205secretkey"

if __name__ == "__main__":

	app.run(host='0.0.0.0',port='80')









