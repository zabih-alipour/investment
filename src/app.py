from flask import Flask
from users import user_controller as user
from category import category_controller as category

app = Flask(__name__)
app.register_blueprint(user.user_blueprint)
app.register_blueprint(category.category_blueprint)

if __name__ == '__main__':
    app.run()
