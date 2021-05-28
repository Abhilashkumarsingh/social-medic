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

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    