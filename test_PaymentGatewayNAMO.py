import unittest
import os
import json
from app import app, db


class PaymentGatewayTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.create_order_data = {
                                    "items":[{"name":"shoes", "qty":10}],
                                    "delivery_note":"need asap plz",
                                    "ordered_by":"sakunia@gmail.com"
                                    }
        self.make_payment_data = {
                "order_id": "f998cf3f-4862-4530-b444-db63a1c72040",
                "amount": "2000",
                "currency": "USD",
                "type": "creditcard",
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "3",
                    "expirationYear": "2020",
                    "cvv": "123"
                }
            }

        with self.app.app_context():
            db.create_all()


    def test_order_creation(self):
        """Test API can create a order (POST request)"""
        res = self.client().post('/order', json=self.create_order_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual('success', json.loads(res.data).get('status'))

    def test_api_can_get_all_orders(self):
        """Test API can get a orders (GET request)."""
        res = self.client().get('/order')
        self.assertEqual(res.status_code, 200)
        self.assertIn('first_order', str(res.data))

    def test_make_payment(self):
        """Test API can make payment(POST request)"""
        res = self.client().post('/payment', json=self.make_payment_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual('success', json.loads(res.data).get('status'))

    def test_make_payment_against_invalid_order(self):
        """Test API validation for invalid order in make payment(POST request)"""
        self.make_payment_data['order_id'] = 'non-existing-id'
        res = self.client().post('/payment', json=self.make_payment_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual('fail', json.loads(res.data).get('status'))

    def test_make_payment_against_invalid_card(self):
        """Test API validation for invalid order in make payment(POST request)"""
        self.make_payment_data['card']['number'] = '123123123'
        res = self.client().post('/payment', json=self.make_payment_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual('fail', json.loads(res.data).get('status'))

    def tearDown(self):
        """teardown all initialized variables."""
        pass

if __name__ == "__main__":
    unittest.main()