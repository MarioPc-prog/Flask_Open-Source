# Authorization for user signing up or logging in/out of our server
from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from . import db
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

            # Get attempted email
            attempted_email = request.form.get('Email')
            # Attempt to find user with this email
            # user, password will return if password hashes correctly
            # and user is verified
            user = serverInterface.findUser(attempted_email)

            # If user exists
            if user:
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


@auth.route('/signup')
def signup():
    return render_template("sign.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")