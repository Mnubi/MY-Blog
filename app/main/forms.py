from wtforms import StringField,TextAreaField, SubmitField, SelectField 
from wtforms.validators import Required, Email, Length
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell Us About Yourself...',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    bio = TextAreaField('About...', validators=[Required(), Length(1, 100)])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post_title = StringField('Pitch title', validators=[Required()])
    
    post_content = StringField('What is in your mind?')
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    blog_title = StringField('Title', validators=[Required()])
    category = SelectField('Category',choices=[('Select a category','Select a category'),('Health', 'Health'),('Lifestyle', 'Lifestyle'),('Sports','Sports'),('Politics','Politics'),('Technology','Technology')], validators=[Required()])
    content = TextAreaField('Body', validators=[Required()])
    created_by= StringField('Author',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write your comment', validators=[Required()])
    submit = SubmitField('Submit')