from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo, Length
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    username = StringField('Enter Your Username', validators=[DataRequired(), Length(min=4, max=20)])
   
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError(message="The Email has already been taken!")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError(message="The username has already been taken")


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class SubscribeForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    submit = SubmitField('subscribe')