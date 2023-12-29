from flask import request
from flask.views import MethodView
from flask_smorest import abort

from models.plantingModel import PlantingModel
from schemas import PlantingSchema
from . import bp

@bp.route('/<planting_id>')
class Planting(MethodView):

    @bp.response(200, PlantingSchema)
    def get(self, planting_id):
        planting=PlantingModel.query.get(planting_id)
        if planting:
            return planting
        else:
            abort(400, message="Planting not found")

    @bp.arguments(PlantingSchema)
    def put(self, planting_data, planting_id):
        planting=PlantingModel.query.get(planting_id)
        if planting:
            planting.from_entry(planting_data)
            planting.commit()
            return{'message':f'{planting.planting_id} updated'},202
        abort(400, message='Invalid Planting ID')

    def delete(self, planting_id):
        planting=PlantingModel.query.get(planting_id)
        if planting:
            planting.delete()
            return{'message':f'{planting.planting_id} deleted'},202
        abort(400, message='Invalid Planting ID')

@bp.route('/')
class PlantingList(MethodView):

    @bp.response(200, PlantingSchema(many=True))
    def get(self):
        return PlantingModel.query.all()
    
    @bp.arguments(PlantingSchema)
    def post(self, planting_data):
        try:
            planting=PlantingModel
            planting.from_entry(planting_data)
            planting.commit()
            return{'message':f'{planting.planting_id} Created'},201
        except:
            abort(400, message='The Seed Has Already Been Planted')