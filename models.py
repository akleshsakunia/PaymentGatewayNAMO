from app import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Order(db.Model):
    # for display
    order_id:str
    items:str
    net_amount:int
    is_paid:bool
    payment_details:str
    ordered_by:str
    ordered_on:str
    requested_turnaround:str

    # table schema
    __tablename__ = 'order'
    order_id = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    items = db.Column(db.String(), nullable=False)
    delivery_note = db.Column(db.String())
    requested_turnaround = db.Column(db.String(), default='1w')
    address= db.Column(db.String())
    ordered_by = db.Column(db.String(), nullable=False)
    ordered_on = db.Column(db.DateTime(), default= datetime.now())
    updated_on = db.Column(db.DateTime(), default=datetime.now(), onupdate=datetime.now)
    payment_method = db.Column(db.String())
    net_amount = db.Column(db.Integer)
    is_paid = db.Column(db.Boolean, default=False)
    payment_details = db.Column(db.String())

    def save(self):
        db.session.add(self)
        db.session.commit()