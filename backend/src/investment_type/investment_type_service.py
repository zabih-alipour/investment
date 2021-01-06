from . import investment_type_repository as repo


def get_investment_types(name):
    return repo.get_investment_types(name)


def get_investment_type_by_id(investment_type_id):
    investment_type = repo.get_investment_type_by_id(investment_type_id)
    if investment_type is None:
        investment_type = {"error": "There is no investment_type with given id"}
    return investment_type


def add_investment_type(investment_type):
    return repo.add_investment_type(investment_type)


def edit_investment_type(investment_type):
    return repo.edit_investment_type(investment_type)


def delete_investment_type(investment_type_id):
    return repo.delete_investment_type(investment_type_id)
