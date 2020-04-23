from flask import Flask
<<<<<<< HEAD
from views import main


debug = True

app = Flask(__name__)
app.register_blueprint(main)


def create_app():

	app.run(debug=debug, host='127.0.0.1')

create_app()
=======
from flask import render_template, request

# create app object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def home_login():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('main_login.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/sign', methods=['POST'])
def sign_post():
    email = request.form.get('email')
    password = request.form.get('password')


#    return f"Email: {email} Password: {password}"


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact', methods=['POST'])
def contact_post():
    email = request.form.get('email')
    subject = request.form.get('subject')
    messageContent = request.form.get('messageContent')


#    return f"Email: {email} Subject: {subject} messageContent: {messageContent}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
>>>>>>> e3dfe25e7b7c617dc8cb5989075ffe5c465daf3d
