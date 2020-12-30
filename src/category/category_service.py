from . import category_repository as repo


def get_categories(name):
    return repo.get_categories(name)


def get_category_by_id(category_id):
    category = repo.get_category_by_id(category_id)
    if category is None:
        category = {"error": "There is no category with given id"}
    return category


def add_category(category):
    return repo.add_category(category)


def edit_category(category):
    return repo.edit_category(category)


def delete_category(category_id):
    return repo.delete_category(category_id)
