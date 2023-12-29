from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.cropModel import CropModel
from models.growerModel import GrowerModel
from models.plantingModel import PlantingModel
from models.plotModel import PlotModel

from resources.crop import bp as crop_bp
api.register_blueprint(crop_bp)

from resources.grower import bp as grower_bp
api.register_blueprint(grower_bp)

from resources.planting import bp as planting_bp
api.register_blueprint(planting_bp)

from resources.plot import bp as plot_bp
api.register_blueprint(plot_bp)