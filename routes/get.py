from flask import Blueprint, render_template

get = Blueprint('get', __name__)


@get.route('/')
def home():
    return render_template('home.html')
