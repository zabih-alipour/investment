from flask import Flask
from users import user_controller as user

app = Flask(__name__)
app.register_blueprint(user.user_blueprint)

if __name__ == '__main__':
    app.run()
