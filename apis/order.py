import json
import uuid

from flask_restful import Resource, request
from flask import jsonify

from app import db
from models import Order as order_table
from validations.order_validator import CreateOrderValidator


class OrderApi(Resource):
    def get(self):
        all_orders = order_table.query.all()
        return jsonify(all_orders)

    def post(self):
        err = CreateOrderValidator().validate(request.json)
        if err:
            return jsonify({'status':'fail', 'response':str(err)})
        else:
            request.json['items'] = str(request.json['items'])
            request.json['order_id'] = str(uuid.uuid4())
            new_order = order_table(**request.json)
            new_order.save()
            return {'status':'success', 'response': 'Order created successfully'}
