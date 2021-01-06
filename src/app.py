from flask import Flask
from users import user_controller as user
from category import category_controller as category
from payment_type import payment_type_controller as payment_type
from payment import payment_controller as payment
from investment import investment_controller as investment
from investment_type import investment_type_controller as investment_type

app = Flask(__name__)
app.register_blueprint(user.user_blueprint)
app.register_blueprint(category.category_blueprint)
app.register_blueprint(payment_type.payment_type_blueprint)
app.register_blueprint(payment.payment_blueprint)
app.register_blueprint(investment.investment_blueprint)
app.register_blueprint(investment_type.investment_type_blueprint)

if __name__ == '__main__':
    app.run()
