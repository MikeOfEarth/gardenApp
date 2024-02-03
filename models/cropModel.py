from app import db
from sqlalchemy import ARRAY, String
from werkzeug.security import generate_password_hash, check_password_hash

class CropModel(db.Model):

    __tablename__ = 'crops'

    crop_name = db.Column(db.String, primary_key = True)
    grow_time = db.Column(db.Integer, nullable = False)
    harvest_num = db.Column(db.Integer, nullable = False)
    harvest_per = db.Column(db.Integer, nullable = False)
    companions = db.Column(db.JSON, nullable = False)
    # companions = db.Column(db.ARRAY(String), nullable = False) <---- I want this to be a list but can't figure out how to work it in sqlalchemy.
    sun_pref = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'<Crop: {self.crop_name}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_entry(self, crop_entry):
        for k, v in crop_entry.items():
            setattr(self, k, v)