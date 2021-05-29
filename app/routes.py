from flask.helpers import url_for
from werkzeug.utils import redirect
from wtforms import validators
from app import app, db
from flask_login import login_user, login_required, current_user, logout_user
from flask import render_template
from app.forms import RegisterForm, LoginForm, MedicalRecordForm
from app.models import Account, MedicalCategory, MedicalRecord

@app.route("/", methods=["POST", 'GET'])
def index():
    form = RegisterForm()

    if form.validate_on_submit():
        account = Account( email=form.email.data )
        account.set_password( form.password.daMedicalRecorda )
        db.session.add(account)
        db.session.commit()
        return redirect(url_for("login"))
        
    return render_template('index.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        account =  Account.query.filter_by(email=form.email.data).first()
        login_user(account)
        return redirect(url_for("dashboard"))
    return render_template("login.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    total = current_user.medical_records.count()
    bangalorean_count = MedicalRecord.query.with_parent(current_user).filter_by(bangalorean="t").count()
    non_bangalorean_count = total-bangalorean_count

    return render_template("dashboard.html", current='dashboard', bangalorean_count=bangalorean_count, non_bangalorean_count=non_bangalorean_count, total=total)

@app.route("/add", methods=['POST', "GET"])
@login_required
def add_medical_record():
    form = MedicalRecordForm()
    if form.validate_on_submit():
        first_name = form.first_name.data.lower()
        last_name = form.last_name.data.lower()
        disease = form.disease.data.lower()
        medical_category = MedicalCategory.query.get(form.medical_category.data)

        medical_record = MedicalRecord(
            first_name=first_name, 
            last_name=last_name, 
            disease=disease, 
            medical_category=medical_category, 
            bangalorean=form.bangalorean.data,
            record_owner=current_user)
            
        db.session.add(medical_record)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("medical_record_form.html", form=form, current='add item')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))