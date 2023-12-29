from flask_smorest import Blueprint

bp = Blueprint('crops', __name__, description='Operations on Crops', url_prefix='/crop')

from . import routes