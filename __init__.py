from flask import Flask
# create app object
app = Flask(__name__)
# register the Blueprint by importing and registering
from views import main
app.register_blueprint(main)



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
