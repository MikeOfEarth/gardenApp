from app import db

from werkzeug.security import generate_password_hash

class GrowerModel(db.Model):

    __tablename__ = 'growers'

    grower_name = db.Column(db.String(30), primary_key = True)
    email = db.Column(db.String(60), nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String(30))

    def __repr__(self):
        return f'<Grower: {self.grower_name}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_entry(self, grower_entry):
        for k, v in grower_entry.items():
            setattr(self, k, v)
            # if k != 'password_hash':
            #     setattr(self, k, v)
            # # else:
            # #     setattr(self, 'password_hash', generate_password_hash(v))