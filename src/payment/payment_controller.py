from flask import Blueprint, json, Response, request

from . import payment_service as service

payment_blueprint = Blueprint('payment', __name__)


@payment_blueprint.route('/payments', methods=['POST'])
def add_payment():
    payment = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty payment!!"}), status=404,
                        mimetype='application/json')
    if payment is not None:
        result = json.dumps(service.add_payment(payment))
        response = Response(result, mimetype='application/json')
    return response


@payment_blueprint.route('/payments', methods=['PUT'])
def edit_payment():
    payment = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty payment!!"}), status=404,
                        mimetype='application/json')
    if payment is not None:
        result = json.dumps(service.edit_payment(payment))
        response = Response(result, mimetype='application/json')
    return response


@payment_blueprint.route('/payments')
def get_payments():
    result = json.dumps(service.get_payments(None))
    return Response(result, mimetype='application/json')


@payment_blueprint.route('/payments/<string:name>')
def get_payments_by_name(name):
    result = json.dumps(service.get_payments(name))
    return Response(result, mimetype='application/json')


@payment_blueprint.route('/payments/<int:payment_id>')
def get_payment_by_id(payment_id):
    result = json.dumps(service.get_payment_by_id(payment_id))
    return Response(result, mimetype='application/json')


@payment_blueprint.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    result = json.dumps(service.delete_payment(payment_id))
    return Response(result, mimetype='application/json')
