from flask_smorest import Blueprint

bp = Blueprint('plantings', __name__, description='Operations on Plantings', url_prefix='/planting')

from . import routes