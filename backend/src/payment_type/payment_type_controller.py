from flask import Blueprint, json, Response, request

from . import payment_type_service as service

payment_type_blueprint = Blueprint('payment_type', __name__)


@payment_type_blueprint.route('/payment_types', methods=['POST'])
def add_payment_type():
    payment_type = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty payment_type!!"}), status=404,
                        mimetype='application/json')
    if payment_type is not None:
        result = json.dumps(service.add_payment_type(payment_type))
        response = Response(result, mimetype='application/json')
    return response


@payment_type_blueprint.route('/payment_types', methods=['PUT'])
def edit_payment_type():
    payment_type = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty payment_type!!"}), status=404,
                        mimetype='application/json')
    if payment_type is not None:
        result = json.dumps(service.edit_payment_type(payment_type))
        response = Response(result, mimetype='application/json')
    return response


@payment_type_blueprint.route('/payment_types')
def get_payment_types():
    result = json.dumps(service.get_payment_types(None))
    return Response(result, mimetype='application/json')


@payment_type_blueprint.route('/payment_types/<string:name>')
def get_payment_types_by_name(name):
    result = json.dumps(service.get_payment_types(name))
    return Response(result, mimetype='application/json')


@payment_type_blueprint.route('/payment_types/<int:payment_type_id>')
def get_payment_type_by_id(payment_type_id):
    result = json.dumps(service.get_payment_type_by_id(payment_type_id))
    return Response(result, mimetype='application/json')


@payment_type_blueprint.route('/payment_types/<int:payment_type_id>', methods=['DELETE'])
def delete_payment_type(payment_type_id):
    result = json.dumps(service.delete_payment_type(payment_type_id))
    return Response(result, mimetype='application/json')
