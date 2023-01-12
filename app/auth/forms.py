from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.auth.models import User

def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')
        
class RegistrationForm(FlaskForm):
    name = StringField("Enter Your Name:",validators=[DataRequired(),Length(3,15,message='Name should be Between 3 Characters to 15 Characters')])
    email = StringField("Enter your E-mail :",validators=[DataRequired(),Length(5),Email(),email_exists])
    password = PasswordField("Enter your Password:",validators=[DataRequired(),Length(8),EqualTo('confirm',message='Password is not Matching')])
    confirm= PasswordField("Confirm Password:",validators=[DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('LogIn')