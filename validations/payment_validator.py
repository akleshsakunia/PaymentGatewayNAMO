from datetime import datetime
import logging

from marshmallow import Schema, fields, ValidationError, validate, validates
from marshmallow.validate import Length, Range, OneOf
from models import Order as order_table

class HandleException(Exception):
    pass

def validate_order(order_id):
    return True

class Card(Schema):
    """
    card schema
    """
    number = fields.Integer(required=True)
    expirationMonth = fields.Integer(required=True, validate=Range(min=1,max=12))
    expirationYear = fields.Integer(required=True, validate=Range(min=datetime.today().year, error="card is expired"))
    cvv = fields.Integer(required=True, validate=Range(min=100,max=999, error="CVV must be three digits long"))

    @validates('number')
    def validate_card_luhn_algo(self,n):
        r = [int(ch) for ch in str(n)][::-1]
        if not (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0:
            raise ValidationError("Card is invalid!")

class PaymentValidator(Schema):
    """
    validates order creation request
    """
    order_id = fields.Str(required=True)
    amount = fields.Integer(required=True)
    currency = fields.Str(required=True)
    type = fields.Str(validate=OneOf(["creditcard", "debitcard"]), required=True)
    card = fields.Nested(Card, required=True)

    @validates('order_id')
    def order_exists(self, value):
        order_exists = order_table.query.filter_by(order_id=value).first()
        if not order_exists:
            raise ValidationError("Order does not exist!")

    def handle_error(self, exc, data, **kwargs):
        #todo: log error to splunk, ES etc
        logging.error(exc.messages)
