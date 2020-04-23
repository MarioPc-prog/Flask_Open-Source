# Authorization for user signing up or logging in/out of our server
from flask import Blueprint, request, redirect, url_for, render_template, flash, session
#from . import db
from backEnd import BackEndInterface

# Define auth blueprint
auth = Blueprint('auth', __name__)

# Connect to server
serverInterface = BackEndInterface("cs205")
serverInterface.connectToServer()

@auth.route("/login/", methods = ["GET", "POST"])
def login():
    error = ""
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
                session['username'] = request.form.get('username')
                flash("You are now logged in")
                # Redirect user
                redirect(url_for("home.html"))

            else:
                error = "Invalid Credentials. Try Again"

        return render_template("main_login.html", error=error)

    except Exception as e:
        flash(e)
        return render_template("main_login.html", error=error)


@auth.route('/sign', methods = ["GET", "POST"])
def signup():
    error = ""
    try:
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if user already exists in database
        if serverInterface.signUser(email, username, password):
            # User has been created, now we want to redirect to login page
            return redirect(url_for('main_login.html'))

        else:
            # User already exists
            flash("Email already exists. Try logging in or make another account")
            redirect(url_for('sign.html'))

    except Exception as e:
        print(e)
    return render_template("sign.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")