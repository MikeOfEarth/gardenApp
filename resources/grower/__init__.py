from flask_smorest import Blueprint

bp = Blueprint('growers', __name__, description='Operations on Growers', url_prefix='/grower')

from . import routes,auth_routes