from app import db
from datetime import datetime
class URL(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    url = db.Column(db.String(2048), nullable=False)
    shortCode = db.Column(db.String(10), unique=True, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now)
    accessCount = db.Column(db.Integer, default=0)
