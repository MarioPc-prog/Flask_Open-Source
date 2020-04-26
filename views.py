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
	error = ""
	print("SIGNUP FUNCTION EXECUTED\n")

	try:
		if request.method == 'POST':
			email = request.form.get('email')
			username = request.form.get('username')
			password = request.form.get('psswrd')
			rpassword = request.form.get('repeatpsswrd')

			if rpassword != password:
				flash("Passwords don't match")
				return redirect(url_for('main.sign'))

			# DEBUGGING
			print(str(email) + '\n' + str(username) + '\n' + str(password) + '\n')
           		 # Check if user already exists in database
			if serverInterface.signUser(str(username), str(password), str(email)):
                       # User has been created, now we want to redirect to login page
				return redirect(url_for('main.home_login'))

			else:
                # User already exists
				print("Views.py: User exists, redirecting to main.sign")
				redirect(url_for('main.sign'))

		redirect(url_for("main.sign"))

	except Exception as e:
		print(e)

	return render_template("sign.html")


@main.route('/fileTransfer')
def fileTransfer():
	return render_template('fileTransfer.html')
#    return f"Email: {email} Password: {password}"


# Define function that checks if a file is allowed to be uploaded
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# # Upload a file - perform basic security checks on it and then save to uploads folder if passed
# @main.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         # If it doesn't, redirect user
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         # Otherwise, request the file
#         file = request.files['file']
#         # If user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         # If file exists and its allowed, make sure its secure and
#         # then save it to the uploads folder
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             #TODO: add the serverInteraction call
#             createRowAssetTable(filename, fileDescription)

#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# Function that returns the given file back to the user by accessing its location
@main.route('/uploads/<filename>')
def uploaded_file(filename):
	# Send from directory will ensure that the given file is really from this
	# location - basic security check that send_file doesn't do
	# Make the upload folder into a absolute path rather than relative
	uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
	return send_from_directory(directory = uploads, attached_file = filename)

# Function that returns file from downloads
# @main.route('/downloads')
# def download_file():
# 	# # Make the download folder into absolute path
# 	# downloads = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
# 	# return send_from_directory(directory = downloads, attached_file = filename)
# 	path = os.getcwd()

# 	return send_file(path+"/static/MattP.jpg",
# 					mimetype='jpg',
# 					attachment_filename='MattP.jpg',
# 					as_attachment=True)

