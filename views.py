from flask import Blueprint, render_template
# create the first grouping for the blueprint
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return '<h1>Test</h1>'
