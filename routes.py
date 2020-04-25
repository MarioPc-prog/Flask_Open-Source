from flask import Blueprint, render_template, redirect
from flask_login import current_user, login_required
from flask import current_app as app
from .assets import compile_auth_assets


# Configure blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)

@main_bp.route('/', methods = ['GET'])
@login_required
def dashboard():
    return render_template('home.html',
                           template = 'home.html',
                           current_user = current_user)