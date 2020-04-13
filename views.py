from flask import Blueprint, render_template, request

# create the first grouping for the blueprint
main = Blueprint('main', __name__)


@main.route('/home/')
def home():
    return render_template('home.html')


@main.route('/blog')
def blog():
    return render_template('blog.html')


@main.route('/sign')
def sign():
    return render_template('sign.html')

@main.route('/sign', methods=['POST'])
def sign_post():
    email = request.form.get('email')
    password = request.form.get('password')
    return f'Email: {email} Password: {password}'
