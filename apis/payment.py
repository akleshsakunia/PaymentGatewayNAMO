from copy import deepcopy
import uuid
from datetime import datetime

from flask_restful import Resource, request
from flask import jsonify

from app import db
from validations.payment_validator import PaymentValidator
from models import Order

def makePayment(payment_info):
    """
    integrate payment gateway logic here, for now we shall just create the payment response
    :param payment_details: card info and amount processing
    :return:
    """
    response = deepcopy(payment_info)
    # remove card info
    response['card'].pop('expirationMonth')
    response['card'].pop('expirationYear')
    response['card'].pop('cvv')
    # add payment meta
    response['authorization_code'] = uuid.uuid4()
    response['time'] = datetime.strftime(datetime.utcnow(), '%Y-%M-%d %H:%M:%S')
    response['status'] = 'success'

    return response

class PaymentApi(Resource):
    def get(self):
        pass

    def post(self):
        err = PaymentValidator().validate(request.json)
        if err:
            return jsonify({'status': 'fail', 'response': str(err)})
        else:
            payment_response = makePayment(request.json)
            if payment_response:
                order_data = Order.query.filter_by(order_id=request.json['order_id']).first()
                order_data.is_paid = True
                order_data.payment_details = str({**payment_response, **request.json})
                order_data.save()
                return jsonify(payment_response)
            else:
                return {'status': 'fail', 'response': 'Error from payment gateway, please try after sometime'}