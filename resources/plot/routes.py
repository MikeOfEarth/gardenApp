from flask import request
from flask.views import MethodView
from flask_smorest import abort

from models.plotModel import PlotModel
from schemas import PlotSchema
from . import bp

@bp.route('/<grid_value>')
class Plot(MethodView):

    @bp.response(200, PlotSchema)
    def get(self, grid_value):
        plot=PlotModel.query.get(grid_value)
        if plot:
            return plot
        else:
            abort(400, message="Plot not found")

    @bp.arguments(PlotSchema)
    def put(self, plot_data, grid_value):
        plot=PlotModel.query.get(grid_value)
        if plot:
            plot.from_entry(plot_data)
            plot.commit()
            return{'message':f'{plot.grid_value} updated'},202
        abort(400, message='Plot Not Found')

    def delete(self, grid_value):
        plot=PlotModel.query.get(grid_value)
        if plot:
            plot.delete()
            return{'message':f'{plot.grid_value} deleted'},202
        abort(400, message='Plot Not Found')

@bp.route('/')
class PlotList(MethodView):

    @bp.response(200, PlotSchema(many=True))
    def get(self):
        return PlotModel.query.all()
    
    @bp.arguments(PlotSchema)
    def post(self, plot_data):
        try:
            plot=PlotModel()
            plot.from_entry(plot_data)
            plot.commit()
            return{'message':f'{plot.grid_value} Created'},201
        except:
            abort(400, message='Plot Already Exists')