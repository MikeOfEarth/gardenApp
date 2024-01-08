from datetime import datetime

from app import db

class PlotModel(db.Model):

    __tablename__ = 'plots'

    # x = db.Column(db.NUMERIC(2, 0), nullable = False)
    # y = db.Column(db.NUMERIC(2, 0), nullable = False)
    x = db.Column(db.Integer, nullable = False)
    y = db.Column(db.Integer, nullable = False)
    grid_value = db.Column(db.String, primary_key = True, default = f'{x},{y}' )
    plot_owner = db.Column(db.String, db.ForeignKey('growers.grower_name'))
    # does owner relationship eliminate? ^
    plot_contents = db.Column(db.Integer, db.ForeignKey('plantings.planting_id'))
    sun = db.Column(db.String(15))
    watered = db.Column(db.Boolean)

    owner = db.relationship('GrowerModel',back_populates = 'owned_plots')

    def __repr__(self):
        return f'<Plot: {self.grid_value}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_entry(self, plot_entry):
        for k, v in plot_entry.items():
            setattr(self, k, v)
        grid = f'{self.x},{self.y}'
        self.grid_value=grid

