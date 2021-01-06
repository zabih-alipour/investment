from . import payment_type_repository as repo


def get_payment_types(name):
    return repo.get_payment_types(name)


def get_payment_type_by_id(payment_type_id):
    payment_type = repo.get_payment_type_by_id(payment_type_id)
    if payment_type is None:
        payment_type = {"error": "There is no payment_type with given id"}
    return payment_type


def add_payment_type(payment_type):
    return repo.add_payment_type(payment_type)


def edit_payment_type(payment_type):
    return repo.edit_payment_type(payment_type)


def delete_payment_type(payment_type_id):
    return repo.delete_payment_type(payment_type_id)
