from flask import Blueprint, json, Response, request

from . import category_service as service

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/categories', methods=['POST'])
def add_category():
    category = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty category!!"}), status=404, mimetype='application/json')
    if category is not None:
        result = json.dumps(service.add_category(category))
        response = Response(result, mimetype='application/json')
    return response


@category_blueprint.route('/categories', methods=['PUT'])
def edit_category():
    category = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty category!!"}), status=404, mimetype='application/json')
    if category is not None:
        result = json.dumps(service.edit_category(category))
        response = Response(result, mimetype='application/json')
    return response


@category_blueprint.route('/categories')
def get_categories():
    result = json.dumps(service.get_categories(None))
    return Response(result, mimetype='application/json')


@category_blueprint.route('/categories/<string:name>')
def get_categories_by_name(name):
    result = json.dumps(service.get_categories(name))
    return Response(result, mimetype='application/json')


@category_blueprint.route('/categories/<int:category_id>')
def get_category_by_id(category_id):
    result = json.dumps(service.get_category_by_id(category_id))
    return Response(result, mimetype='application/json')


@category_blueprint.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    result = json.dumps(service.delete_category(category_id))
    return Response(result, mimetype='application/json')
