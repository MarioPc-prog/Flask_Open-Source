from flask import Blueprint, render_template
# create the first grouping for the blueprint
main = Blueprint('main', __name__)


@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/sign')
def sign():
    return render_template('sign.html')