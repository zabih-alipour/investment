from flask import Blueprint, json, Response, request

from . import investment_service as service

investment_blueprint = Blueprint('investment', __name__)


@investment_blueprint.route('/investments', methods=['POST'])
def add_investment():
    investment = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty investment!!"}), status=404,
                        mimetype='application/json')
    if investment is not None:
        result = json.dumps(service.add_investment(investment))
        response = Response(result, mimetype='application/json')
    return response


@investment_blueprint.route('/investments', methods=['PUT'])
def edit_investment():
    investment = request.get_json()
    response = Response(json.dumps({"error": "Can not save empty investment!!"}), status=404,
                        mimetype='application/json')
    if investment is not None:
        result = json.dumps(service.edit_investment(investment))
        response = Response(result, mimetype='application/json')
    return response


@investment_blueprint.route('/investments')
def get_investments():
    result = json.dumps(service.get_investments(None))
    return Response(result, mimetype='application/json')


@investment_blueprint.route('/investments/<string:name>')
def get_investments_by_name(name):
    result = json.dumps(service.get_investments(name))
    return Response(result, mimetype='application/json')


@investment_blueprint.route('/investments/<int:investment_id>')
def get_investment_by_id(investment_id):
    result = json.dumps(service.get_investment_by_id(investment_id))
    return Response(result, mimetype='application/json')


@investment_blueprint.route('/investments/<int:investment_id>', methods=['DELETE'])
def delete_investment(investment_id):
    result = json.dumps(service.delete_investment(investment_id))
    return Response(result, mimetype='application/json')
