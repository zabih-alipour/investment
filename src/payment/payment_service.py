from . import payment_repository as repo


def get_payments(name):
    return repo.get_payments(name)


def get_payment_by_id(payment_id):
    payment = repo.get_payment_by_id(payment_id)
    if payment is None:
        payment = {"error": "There is no payment with given id"}
    return payment


def add_payment(payment):
    return repo.add_payment(payment)


def edit_payment(payment):
    return repo.edit_payment(payment)


def delete_payment(payment_id):
    return repo.delete_payment(payment_id)
