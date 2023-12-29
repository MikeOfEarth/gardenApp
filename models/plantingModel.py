from datetime import datetime

from app import db

class PlantingModel(db.Model):

    __tablename__ = 'plantings'

    planting_id = db.Column(db.Integer, primary_key = True)
    crop_name = db.Column(db.String, db.ForeignKey('crops.crop_name'), nullable = False)
    # planted will be datetime, cover later
    planted_dt = db.Column(db.String)
    # harvestable_when = plantings.planted_dt + crops.grow_time (will check time adition rules) if plots.watered = True. If false wait till True, planted_dt timestamps current time, set h_w = p.p_dt = c.g_t
    # if crops.harvest_num > 1, reset p_dt clock upon harvest with h_w = p.p_dt + (c.g_t/4)
    harvestable_when = db.Column(db.String)
    # companioned set true when checking grids at x+-1 and y+-1. if plots.grid.content.crop_name in plantings.crop_name.companions, companioned = True
    companioned = db.Column(db.Boolean)
    # light_match set true when planted.crop_name.sun_pref = planted.id>plots.content.sun
    light_match = db.Column(db.Boolean)


    def __repr__(self):
        return f'<Planting: {self.planting_id}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_entry(self, planting_entry):
        for k, v in planting_entry.items():
            setattr(self, k, v)