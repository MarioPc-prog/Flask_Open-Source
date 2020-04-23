# Authorization for user signing up or logging in/out of our server
from flask import Blueprint, request, redirect, url_for, render_template, flash
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
            # email is in  reference to value = "{{request.form.email}}"
            # on login.html within the input html tag in the form
            attempted_username = request.form['username']
            attempted_email = request.form['email']
            attempted_password = request.form['password']

            # TODO - security on username/password
            # TODO - perform password hashing to "unhash" the password from the
            # TODO   database
            # Find user from database
            user, password = BackEndInterface.findUser()

            if attempted_email == "admin" and attempted_password == "password":
                # homepage is just wherever you want logged in users to be redirected
                return redirect(url_for('homepage'))
            else:
                error = "Invalid credentials"

        return render_template("login.html", error=error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


@auth.route('/signup')
def signup():
    return render_template("sign.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")