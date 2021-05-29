from app import app, db
from app.models import Account, MedicalCategory, MedicalRecord

@app.shell_context_processor
def make_shellp():
    return { "app":app, "MedicalCategory":MedicalCategory, "MedicalRecord":MedicalRecord, "db":db  }