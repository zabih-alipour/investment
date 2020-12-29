from . import user_repository as repo


def get_users(name):
    return repo.get_users(name)


def get_user_by_id(user_id):
    user = repo.get_user_by_id(user_id)
    if user is None:
        user = {"error": "There is no user with given id"}
    return user


def add_user(user):
    return repo.add_user(user)


def edit_user(user):
    return repo.edit_user(user)


def delete_user(user_id):
    return repo.delete_user(user_id)
