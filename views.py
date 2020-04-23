from flask import Blueprint, render_template, request, redirect, url_for


from backEnd import BackEndInterface

import ServerInteraction

serverInterface = BackEndInterface("205final")
serverInterface.connectToServer()

# create the first grouping for the blueprint

main = Blueprint("main",
                    __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static"
                    )


@main.route('/')
def home():

	assetList = serverInterface.selectXfromAssets(5)
	return render_template('home.html', assetList=assetList)

@main.route('/download', methods=['POST'])
def home_download():

	assetList = serverInterface.selectXfromAssets(5)

	fileName = request.get(fileName)
	print(fileName) #For testing, delete after testing

	assetLocation = serverInterface.selectAssetToDownload(fileName)

	#TODO: talk to Ben about getting the download to run. 
	ServerInteraction.download_file(assetLocation)

	return "<h1>File Downloaded </h1>" #Change this to redirect if time allows






@main.route('/', methods=['POST'])
def home_login():
	email = request.form.get('email')
	password = request.form.get('password')
	return render_template('main_login.html')


@main.route('/about')
def about():
	return render_template('about.html')


@main.route('/sign')
def sign():
	return render_template('sign.html')

@main.route('/contact')
def contact():
	return render_template('contact.html')

@main.route('/contact', methods=['POST'])
def contact_post():
	email = request.form.get('email')
	subject = request.form.get('subject')
	messageContent = request.form.get('messageContent')

	# function call - give that to backend
	return f"Email: {email} Subject: {subject} messageContent: {messageContent}" 



@main.route('/sign', methods=['POST'])
def sign_post():
	email = request.form.get('email')
	password = request.form.get('password')

	return f'Email: {email} Password: {password}'

@main.route('/fileTransfer')
def fileTransfer():
	return render_template('fileTransfer.html')
#    return f"Email: {email} Password: {password}"


