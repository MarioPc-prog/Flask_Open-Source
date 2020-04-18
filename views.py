from flask import Blueprint, render_template, request
# create the first grouping for the blueprint
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('About.html')

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

	return f"Email: {email} Subject: {subject} messageContent: {messageContent}"

