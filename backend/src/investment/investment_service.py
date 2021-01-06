from . import investment_repository as repo


def get_investments(name):
    return repo.get_investments(name)


def get_investment_by_id(investment_id):
    investment = repo.get_investment_by_id(investment_id)
    if investment is None:
        investment = {"error": "There is no investment with given id"}
    return investment


def add_investment(investment):
    return repo.add_investment(investment)


def edit_investment(investment):
    return repo.edit_investment(investment)


def delete_investment(investment_id):
    return repo.delete_investment(investment_id)
