from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
#     submit = SubmitField('Save')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category',validators=[DataRequired()])
    blog = TextAreaField('Your blog', validators=[DataRequired()])
    
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')


