from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import InputRequired, Email
from app.models import Account
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up")

    def validate_email(form, field):
        if Account.query.filter_by(email=field.data).first():
            raise ValidationError('Email Exists')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember_me = BooleanField("Remeber Me")

    def validate_email(form, field):
        account = Account.query.filter_by(email=field.data).first()
        if account is None:
            raise ValidationError("Email Does Not Exist")
        if account.check_password(form.password.data) == False :
            raise ValidationError("Email does not match Password")
