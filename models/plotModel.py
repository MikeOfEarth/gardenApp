from datetime import datetime

from app import db

class PlotModel(db.Model):

    __tablename__ = 'plots'

    # grid_value = ",".join([str(x), str(y)])
    grid_value = db.Column(db.Integer, primary_key = True)
    # x = db.Column(db.NUMERIC(2, 0), nullable = False)
    # y = db.Column(db.NUMERIC(2, 0), nullable = False)
    x = db.Column(db.Integer, nullable = False)
    y = db.Column(db.Integer, nullable = False)
    plot_owner = db.Column(db.String, db.ForeignKey('growers.grower_name'))
    plot_contents = db.Column(db.Integer, db.ForeignKey('plantings.planting_id'))
    sun = db.Column(db.String(15))
    watered = db.Column(db.Boolean)

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
            if k!='grid_value':
                setattr(self, k, v)
            else:
                setattr(self,'grid_value',(",".join([str(self['x']), str(self['y'])])))

