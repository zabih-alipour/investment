from flask import Blueprint, json, Response, request

from . import investment_type_service as service

investment_type_blueprint = Blueprint('investment_type', __name__)


@investment_type_blueprint.route('/investment_types', methods=['POST'])
def add_investment_type():
    investment_type = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty investment_type!!"}), status=404,
                        mimetype='application/json')
    if investment_type is not None:
        result = json.dumps(service.add_investment_type(investment_type))
        response = Response(result, mimetype='application/json')
    return response


@investment_type_blueprint.route('/investment_types', methods=['PUT'])
def edit_investment_type():
    investment_type = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty investment_type!!"}), status=404,
                        mimetype='application/json')
    if investment_type is not None:
        result = json.dumps(service.edit_investment_type(investment_type))
        response = Response(result, mimetype='application/json')
    return response


@investment_type_blueprint.route('/investment_types')
def get_investment_types():
    result = json.dumps(service.get_investment_types(None))
    return Response(result, mimetype='application/json')


@investment_type_blueprint.route('/investment_types/<string:name>')
def get_investment_types_by_name(name):
    result = json.dumps(service.get_investment_types(name))
    return Response(result, mimetype='application/json')


@investment_type_blueprint.route('/investment_types/<int:investment_type_id>')
def get_investment_type_by_id(investment_type_id):
    result = json.dumps(service.get_investment_type_by_id(investment_type_id))
    return Response(result, mimetype='application/json')


@investment_type_blueprint.route('/investment_types/<int:investment_type_id>', methods=['DELETE'])
def delete_investment_type(investment_type_id):
    result = json.dumps(service.delete_investment_type(investment_type_id))
    return Response(result, mimetype='application/json')
