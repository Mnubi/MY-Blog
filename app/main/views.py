from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User
from flask_login import login_required,current_user
from .. import db


#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    return render_template('index.html')

class Blog(db.Model):
    _tablename_='blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    content= db.Column(db.String(255))
    author= db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
          
     # save/delete blog

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()    

    def repr(self):
        return f'Blog {self.title}'

class Blog(db.Model):
    _tablename_='blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    content= db.Column(db.String(255))
    created_by= db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        
     # save/delete blog

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()    

    @classmethod
    def get_blogs(cls,id):
            blogs =Blog.query.filter_by(blog_id=id).all()
            return blogs    

    def repr(self):
        return f'Blog {self.title}'