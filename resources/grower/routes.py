from flask import request
from flask.views import MethodView
from flask_smorest import abort

from models.growerModel import GrowerModel
from schemas import GrowerSchema
from . import bp

@bp.route('/<grower_name>')
class Grower(MethodView):

    @bp.response(200, GrowerSchema)
    def get(self, grower_name):
        grower=GrowerModel.query.get(grower_name)
        if grower:
            return grower
        else:
            abort(400, message="Grower not found")

    @bp.arguments(GrowerSchema)
    def put(self, grower_data, grower_name):
        grower=GrowerModel.query.get(grower_name)
        if grower:
            grower.from_entry(grower_data)
            grower.commit()
            return{'message':f'{grower.grower_name} updated'},202
        abort(400, message='Invalid Grower Name')

    def delete(self, grower_name):
        grower=GrowerModel.query.get(grower_name)
        if grower:
            grower.delete()
            return{'message':f'{grower.grower_name} deleted'},202
        abort(400, message='Invalid Grower Name')

@bp.route('/')
class GrowerList(MethodView):

    @bp.response(200, GrowerSchema(many=True))
    def get(self):
        return GrowerModel.query.all()
    
    @bp.arguments(GrowerSchema)
    def post(self, grower_data):
        try:
            grower=GrowerModel
            grower.from_entry(grower_data)
            grower.commit()
            return{'message':f'{grower.grower_name} Created'},201
        except:
            abort(400, message='Grower Name Already In System')