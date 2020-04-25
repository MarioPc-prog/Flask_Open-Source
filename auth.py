# Authorization for user signing up or logging in/out of our server
import gc
import wrap

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from . import db
from backEnd import BackEndInterface
from flask_login import LoginManager, login_user, logout_user, current_user
from flask import current_app as app

# Define auth blueprint
auth = Blueprint('auth_bp', __name__,
                 template_folder='templates',
                 static_folder='static')
compile_auth_assets(app)

# Connect to server
serverInterface = BackEndInterface("205final")
serverInterface.connectToServer()

@auth.route("/main_login/", methods = ["GET", "POST"])
def login():
    error = ""
    # Bypass if user is already logged in
    if current_user.is_authenticated:
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
                session['username'] = request.form.get('username')
                flash("You are now logged in")
                next_page = request.args.get('next')
                # Redirect user
                # user has correct credentials
                return redirect(url_for("home.html"))

            else:
                error = "Invalid Credentials. Try Again"
                return redirect(url_for("main_login.html", error=error))

        return redirect(url_for("main_login.html", error = error))

    except Exception as e:
        flash(e)
        return redirect(url_for("main_login.html", error=error))


@auth.route('/sign', methods = ["GET", "POST"])
def signup():
    error = ""
    try:
        if request.method == 'POST':
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

        redirect(url_for("sign.html"))

    except Exception as e:
        print(e)
    return render_template("sign.html")

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You must log in first")
            return redirect(url_for("main_login"))

@auth.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out")
    gc.collect()
    return redirect(url_for("home"))

def create_app():

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Checks if user is logged-in on every page load."""
    if user_id is not None:
        return getUsername(email)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('main_login.html'))
