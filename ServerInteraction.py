# This file will handle uploading/downloading files using Flask
# It will include all server interaction functions allowing flask to speak to the backend
# and thus allowing us to serve files to the user
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, current_app
from werkzeug.utils import secure_filename

# Define folder that will contain uploads within the server
# Temp path - will change upon going live
UPLOAD_FOLDER = '/var/www/files/uploads'
DOWNLOAD_FOLDER = '/var/www/files/downloads'
# Will allow more extensions going forward - this is for testing
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


# Define function that checks if a file is allowed to be uploaded
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Upload a file - perform basic security checks on it and then save to uploads folder if passed
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        # If it doesn't, redirect user
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # Otherwise, request the file
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # If file exists and its allowed, make sure its secure and
        # then save it to the uploads folder
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # TODO - Make a database entry that includes the filename and other info
            createRowFile(filename, )
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Function that returns the given file back to the user by accessing its location
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Send from directory will ensure that the given file is really from this
    # location - basic security check that send_file doesn't do
    # Make the upload folder into a absolute path rather than relative
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory = uploads, attached_file = filename)

# Function that returns file from downloads
@app.route('/downloads/<filename>')
def download_file(filename):
    # TODO - Check database for filename, return path and necessary info

    # Make the download folder into absolute path
    downloads = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
    return send_from_directory(directory = downloads, attached_file = filename)


@app.route('/login/', methods = ["GET", "POST"])
def login_page():
    error = ""
    try:
        if request.method == "POST":
            # username is in  reference to value = "{{request.form.username}}"
            # on login.html within the input html tag in the form
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            # Now we've got whatever they've posted

            # DEBUGGING
            #flash(attempted_username)
            #flash(attempted_password)

            # Replace admin and password with the database credentials
            # Search db for username AFTER cleaning username
            # get hash and encrypted password for username
            # make sure it equals given password
            if attempted_username == "admin" and attempted_password == "password":
                # homepage is just wherever you want logged in users to be redirected
                return redirect(url_for('homepage'))
            else:
                error = "Invalid credentials"

        return render_template("login.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error = error)