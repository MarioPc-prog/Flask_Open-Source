from flask import Flask

global app

debug = True
app = Flask(__name__)
# app.register_blueprint(main)

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager


# from backEnd import BackEndInterface

# import ServerInteraction

# serverInterface = BackEndInterface("205final")
# serverInterface.connectToServer()

login_manager = LoginManager()

# create the first grouping for the blueprint

# main = Blueprint("main",
#                     __name__,
#                     template_folder="templates",
#                     static_folder="static",
#                     static_url_path="/static"
#                     )


@app.route('/')
def home():

	#assetList = serverInterface.selectXfromAssets(5)
	assetList = [("id","fileName","fileLocation","fileDescription","fileImage")]
	return render_template('home.html', assetList=assetList)

@app.route('/download', methods=['POST'])
def home_download():

	# assetList = serverInterface.selectXfromAssets(5)

	# fileName = request.get(fileName)
	# print(fileName) #For testing, delete after testing

	# assetLocation = serverInterface.selectAssetToDownload(fileName)

	# #TODO: talk to Ben about getting the download to run. 
	# ServerInteraction.download_file(assetLocation)

	return "<h1>File Downloaded </h1>" #Change this to redirect if time allows






@app.route('/', methods=['POST'])
def home_login():
	email = request.form.get('email')
	password = request.form.get('password')
	return render_template('main_login.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_post():
	email = request.form.get('email')
	subject = request.form.get('subject')
	messageContent = request.form.get('messageContent')

	# function call - give that to backend
	return redirect(url_for('main.home')) #Example redirect 



@app.route('/sign', methods=['POST'])
def sign_post():
	email = request.form.get('email')
	password = request.form.get('password')

	return f'Email: {email} Password: {password}'

@app.route('/fileTransfer')
def fileTransfer():
	return render_template('fileTransfer.html')
#    return f"Email: {email} Password: {password}"


def create_app():

	app.run(debug=debug, host='0.0.0.0:80')

	app.config.from_object('config.Config')
	login_manager.init_app(app)

	with app.app_context():
		from . import routes
		from . import auth

		app.register_blueprint(routes.main_bp)
		app.register_blueprint(auth.auth_bp)

		return app

# create_app()

# For local host running only - otherwise comment out 
# def create_app():

# 	app.run(debug=debug, host='127.0.0.1')

# create_app()

if __name__ == "__main__":
	app.run(debug=debug, host = '127.0.0.1')








