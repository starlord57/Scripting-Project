from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserRegisterationForm(FlaskForm):
    def post(self)
        username = StringField('Username',
                            validators=[DataRequired()])
        email = StringField('Email',
                            validators=[DataRequired(), Email() ])
        password = PasswordField('Password', validators=[DataRequired()] )
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')

class UserLoginForm(FlaskForm):
        username = StringField('Username',
                            validators=[DataRequired(),Length(min = 2, max=20 )])

        email = StringField('Email',
                            validators=[DataRequired(), Email() ])
        password = PasswordField('Password', validators=[DataRequired()] )
        remember = BooleanField('Remember Me')
        submit = SubmitField('login')

class RestaurantRegisterForm(FlaskForm):
        restname = StringField('Restname',
                                validators=[DataRequired(),Length(min = 2, max=20)])
        email = StringField('Email',
                                validators=[DataRequired(), Email() ])
        password = PasswordField('Password', validators=[DataRequired()] )
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')

class RestLoginForm(FlaskForm):
        restname = StringField('Username',
                            validators=[DataRequired(),Length(min = 2, max=20 )])

        email = StringField('Email',
                            validators=[DataRequired(), Email() ])
        password = PasswordField('Password', validators=[DataRequired()] )
        remember = BooleanField('Remember Me')
        submit = SubmitField('login')

class AdminLoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(),Length(min = 2, max=20 )])

    email = StringField('Email',
                        validators=[DataRequired(), Email() ])
    password = PasswordField('Password', validators=[DataRequired()] )
    submit = SubmitField('login')
