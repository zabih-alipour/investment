from flask import Blueprint, request

from ..users import user_service as service

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/users')
def get_users():
    query_string = request.query_string
    return service.get_users()
