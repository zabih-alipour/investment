from flask import Blueprint, json, Response, request

from . import user_service as service

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty user!!"}), status=404, mimetype='application/json')
    if user is not None:
        result = json.dumps(service.add_user(user))
        response = Response(result, mimetype='application/json')
    return response


@user_blueprint.route('/users', methods=['PUT'])
def edit_user():
    user = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty user!!"}), status=404, mimetype='application/json')
    if user is not None:
        result = json.dumps(service.edit_user(user))
        response = Response(result, mimetype='application/json')
    return response


@user_blueprint.route('/users')
def get_users():
    result = json.dumps(service.get_users(None))
    return Response(result, mimetype='application/json')


@user_blueprint.route('/users/<string:name>')
def get_users_by_name(name):
    result = json.dumps(service.get_users(name))
    return Response(result, mimetype='application/json')


@user_blueprint.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    result = json.dumps(service.get_user_by_id(user_id))
    return Response(result, mimetype='application/json')


@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = json.dumps(service.delete_user(user_id))
    return Response(result, mimetype='application/json')
