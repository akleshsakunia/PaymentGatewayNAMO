import logging

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow.validate import Length, Range, OneOf

def validate_order(order_id):
    return True

class Item(Schema):
    """
    item schema
    """
    name = fields.Str(required=True, validate=Length(max=100))
    qty = fields.Number(required=True, validate=Range(min=1,max=20))
    price = fields.Number()

class Address(Schema):
    """
    address schema
    """
    addr1 = fields.Str(required=True, validate=Length(max=100))
    addr2 = fields.Str(validate=Length(max=100))
    city = fields.Str(required=True, validate=Length(max=100))
    State = fields.Str(required=True, validate=Length(max=100))
    zip_code = fields.Str(required=True, validate=Length(max=100))


class CreateOrderValidator(Schema):
    """
    validates order creation request
    """
    items = fields.List(fields.Nested(Item), required=True)
    delivery_note = fields.Str(validate=Length(max=1000))
    requested_turnaround = fields.Str(validate=OneOf(["1d", "2d", "1w"]))
    address = fields.Nested(Address)
    ordered_by = fields.Str(required=True) #todo: should be taken from user logged in entity

    # def handle_error(self, exc, data, **kwargs):
    #     #todo: log error in db
    #     logging.error(exc.messages)
    #     raise HandleException("An error occurred with input: {0}".format(data))

class UpdateOrderValidator(Schema):
    """
    validates order updation request
    """
    order_id = fields.Str(validate=validate_order)
    items = fields.List(fields.Nested(Item), required=True)
    delivery_note = fields.Str(validate=Length(max=1000))
    requested_turnaround = fields.Str(validate=validate.OneOf(["1d", "2d", "1w"]))
    address = fields.Nested(Address)
    updated_by = fields.Str(required=True)  # todo: should be taken from user logged in entity

    # def handle_error(self, exc, data, **kwargs):
    #     # todo: log error in db
    #     logging.error(exc.messages)
    #     raise HandleException("An error occurred with input: {0}".format(data))
