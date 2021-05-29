from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(id):
    return Account.query.get(id)

class Account(db.Model, UserMixin):
    id = db.Column( db.Integer, primary_key=True, nullable=False)
    email = db.Column( db.String, index=True, nullable=False, unique=True)
    password = db.Column( db.String, nullable=False)

    medical_records = db.relationship( "MedicalRecord", backref="record_owner", lazy='dynamic')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"{self.id} - {self.email}"

class MedicalCategory(db.Model):
    id = db.Column( db.Integer, primary_key=True, nullable=False)
    category_name = db.Column( db.String(), nullable=False, unique=True)
    medical_records = db.relationship( "MedicalRecord", backref="medical_category", lazy='dynamic') 

    @staticmethod
    def get_all_categories():
        return MedicalCategory.query.all()

    def __repr__(self):
        return f"{self.id} - {self.category_name}"

class MedicalRecord(db.Model):
    id = db.Column( db.Integer, primary_key=True, nullable=False)
    first_name = db.Column( db.String, nullable=False)
    last_name = db.Column( db.String, nullable=False)
    disease = db.Column( db.String, nullable=False)
    bangalorean = db.Column( db.Boolean, nullable=False)

    medical_category_id =  db.Column(db.Integer, db.ForeignKey("medical_category.id"), nullable=False)
    record_owner_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)