from flask_smorest import Blueprint

bp = Blueprint('plots', __name__, description='Operations on Plots', url_prefix='/plot')

from . import routes

