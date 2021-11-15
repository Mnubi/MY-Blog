from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Quote,Blog
from flask_login import current_user
from .. import db,photos
from .forms import UpdateProfile

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
