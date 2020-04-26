import os

from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, current_app, flash, send_file

from werkzeug.utils import secure_filename


from backEnd2 import BackEndInterface

import ServerInteraction

serverInterface = BackEndInterface("205final")
# serverInterface.connectToServer()

# create the first grouping for the blueprint

main = Blueprint("main",
                    __name__,
                    template_folder="templates",
                    static_folder="static",
                    static_url_path="/static"
                    )

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@main.route('/')
def home():

	assetList = serverInterface.selectXfromAssets(5)
	#assetList = [("id","fileName","fileLocation","fileDescription","fileImage")]
	return render_template('home.html', assetList=assetList)

@main.route('/download-file2/<folder>/<name>', methods=['GET'])
def home_download(folder,name):

	path = os.getcwd()
	
	
	
	print("\n\n" + str(name)+"\n\n")
	
	
	return send_file(str(folder)  + "/" + str(name),
					attachment_filename=str(name),
					as_attachment=True)


@main.route('/', methods=['POST'])
def home_login():
	email = request.form.get('email')
	password = request.form.get('password')
	return render_template('fileTransfer.html')


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
	return redirect(url_for('main.home')) #Example redirect 



@main.route('/sign', methods=['POST'])
def sign_post():
	email = request.form.get('email')
	password = request.form.get('password')

	return '<h1>Email has been sent</h1>'

@main.route('/fileTransfer')
def fileTransfer():
	return render_template('fileTransfer.html')
#    return f"Email: {email} Password: {password}"


# Define function that checks if a file is allowed to be uploaded
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





@main.route('/upload-file', methods =['POST'])
def upload_file():
	print('\n\nROUTE HIT \n\n')
	
	f = request.files['filename']
	fileDescr = request.form.get('fileDescription')

	print('\n\n' + str(f.filename) + '\n\n' + str(fileDescr) + '\n\n')

	path = os.path.join(current_app.root_path,'static/')

	f.save(os.path.join(path,secure_filename(f.filename)))

	serverInterface.createRowAssetTable(f.filename,fileDescr)

	return 'file uploaded succesfully'
