import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object(config.DevConfig)

db = SQLAlchemy(app)

from models import Order
# db.create_all()

api = Api(app)


# importing API's
try:
    from apis.order import OrderApi
    from apis.payment import PaymentApi
except Exception as e:
    print('exception hai', e)

api.add_resource(OrderApi, '/order')
api.add_resource(PaymentApi, '/payment')
