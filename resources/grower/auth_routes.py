from flask_jwt_extended import create_access_token

from models.growerModel import GrowerModel

from . import bp 
from schemas import GrowerLogin

@bp.post('/login')
@bp.arguments(GrowerLogin)
def login(grower_data):
    active_grower = GrowerModel.query.filter_by(grower_name=grower_data['grower_name']).first()
    print(active_grower)
    if active_grower and active_grower.check_password(grower_data['password']):
        token = create_access_token(active_grower.grower_name)
        return{'token' : token}
    return {'message' : 'Invalid Grower Data'}