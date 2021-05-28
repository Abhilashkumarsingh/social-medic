from flask.helpers import url_for
from werkzeug.utils import redirect
from wtforms import validators
from app import app, db
from flask_login import login_user, login_required
from flask import render_template
from app.forms import RegisterForm, LoginForm
from app.models import Account

@app.route("/", methods=["POST", 'GET'])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        account = Account( email=form.email.data )
        account.set_password( form.password.data )
        db.session.add(account)
        db.session.commit()
        return redirect(url_for("login"))
        
    return render_template('index.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        account =  Account.query.filter_by(email=form.email.data).first()
        login_user(account)
        return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    return "LOL"