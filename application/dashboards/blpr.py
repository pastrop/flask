from flask import Blueprint
from flask import current_app as app

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


# Set up a Blueprint
test = Blueprint('test', __name__)

@test.route('/test', methods=['GET'])
@jwt_required
def admin():
    """Admin page route."""
    return 'testing dashboard'