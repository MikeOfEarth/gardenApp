from marshmallow import Schema, fields

class CropSchema(Schema):
    crop_name = fields.Str(required = True)
    grow_time = fields.Str(required = True)
    harvest_num = fields.Str(required = True)
    harvest_per = fields.Str(required = True)
    companions = fields.List(fields.Str(),required = True)
    sun_pref = fields.Str(required = True)

class GrowerSchema(Schema):
    grower_name = fields.Str(required = True)
    email = fields.Str(required = True)
    password = fields.Str(required = True, load_only=True)

class GrowerLogin(Schema):
    grower_name = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)

class PlantingSchema(Schema):
    planting_id = fields.Str(dump_only=True)
    crop_name = fields.Str(required = True)
    planted_dt = fields.DateTime(dump_only = True)
    harvestable_when = fields.Str(dump_only = True)
    companioned = fields.Str(dump_only = True)
    light_match = fields.Str(dump_only = True)

class PlotSchema(Schema):
    grid_value = fields.Str(dump_only = True)
    x = fields.Str(required = True)
    y = fields.Str(required = True)
    plot_owner = fields.Str(required = True)
    plot_contents = fields.Str(required = True)
    sun = fields.Str()
    watered = fields.Bool()