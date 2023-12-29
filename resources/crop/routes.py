from flask import request
from flask.views import MethodView
from flask_smorest import abort

from models.cropModel import CropModel
from schemas import CropSchema
from . import bp

@bp.route('/<crop_name>')
class Crop(MethodView):

    @bp.response(200, CropSchema)
    def get(self,crop_name):
        crop = CropModel.query.get(crop_name)
        if crop:
            return crop
        else:
            abort(400, message='Crop not found')

    @bp.arguments(CropSchema)
    def put(self, crop_data, crop_name):
        crop = CropModel.query.get(crop_name)
        # ask about this
        if crop:
            crop.from_entry(crop_data)
            crop.commit()
            return { 'message':f'{crop.crop_name} updated'}, 202
        abort(400, message = "Crop not found")

    def delete(self, crop_name):
        crop = CropModel.query.get(crop_name)
        if crop:
            crop.delete()
            return { 'message':f'{crop.crop_name} deleted'}, 202
        abort(400, message = "Crop not found")

@bp.route('/')
class CropList(MethodView):

    @bp.response(200, CropSchema(many = True))
    def get(self):
        return CropModel.query.all()
    
    @bp.arguments(CropSchema)
    def post(self,crop_data):
        try:
            crop = CropModel()
            crop.from_entry(crop_data)
            crop.commit()
            return { 'message' : f'{crop_data["crop_name"]} created'}, 201
        except:
            abort(400, message = f'{crop_data["crop_name"]} already in')



# get
# add
# change
# delet