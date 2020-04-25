from flask import Flask

global app

debug = True

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager

from backEnd import BackEndInterface

# import ServerInteraction

# Initialize server connection
serverInterface = BackEndInterface("205final")
serverInterface.connectToServer()



# create the first grouping for the blueprint

main = Blueprint("main",
                    __name__,
                     template_folder="templates",
                     static_folder="static",
                     static_url_path="/static"
                     )


def create_app():
    # create app object
    app = Flask(__name__)

    # register the Blueprint by importing and registering
    from .views import main

    app.register_blueprint(main)
    app.config["DEBUG"] = debug

    return app


@app.route('/')
def home():
    # assetList = serverInterface.selectXfromAssets(5)
    assetList = [("id", "fileName", "fileLocation", "fileDescription", "fileImage")]
    return render_template('home.html', assetList=assetList)


@app.route('/download', methods=['POST'])
def home_download():
    # assetList = serverInterface.selectXfromAssets(5)

    # fileName = request.get(fileName)
    # print(fileName) #For testing, delete after testing

    # assetLocation = serverInterface.selectAssetToDownload(fileName)

    # #TODO: talk to Ben about getting the download to run.
    # ServerInteraction.download_file(assetLocation)

    return "<h1>File Downloaded </h1>"  # Change this to redirect if time allows


@app.route('/login', methods=['GET', 'POST'])
def home_login():
    error = ""
    # Bypass if user is already logged in
    if session['logged_in']:
        return redirect(url_for('home.html'))
    try:
        if request.method == "POST":
            # Get attempted email and password
            attempted_email = request.form.get('Email')
            attempted_password = request.form.get("password")
            # Attempt to find user with this email
            # Will return true if user is verified
            # use email because it is unique to every user
            if serverInterface.verifyUser(attempted_email, attempted_password):
                # Define a new session variable
                session['logged_in'] = True
                session['userId'] = serverInterface.getUserID(attempted_email)
                flash("You are now logged in")
                return redirect(url_for("main.home"))

            else:
                error = "Invalid Credentials. Try Again"
                return redirect(url_for("main.home_login", error=error))

        return redirect(url_for("main.home_login", error=error))

    except Exception as e:
        flash(e)
        return redirect(url_for("main.home_login", error=error))


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
    return redirect(url_for('main.home'))  # Example redirect


@app.route('/sign', methods=['POST'])
def sign_post():
    email = request.form.get('email')
    password = request.form.get('password')
    return redirect(url_for('main.home'))
    #return f'Email: {email} Password: {password}'


@app.route('/fileTransfer')
def fileTransfer():
    return render_template('fileTransfer.html')


#    return f"Email: {email} Password: {password}"


# def create_app():

#	app.run(debug=debug, host='0.0.0.0:80')

#	app.config.from_object('config.Config')

#	app.config["TESTING"] = True
#


# create_app()

# For local host running only - otherwise comment out 
# def create_app():

# 	app.run(debug=debug, host='127.0.0.1')

#create_app()

if __name__ == "__main__":

    app.run(debug=debug, host='127.0.0.1')
