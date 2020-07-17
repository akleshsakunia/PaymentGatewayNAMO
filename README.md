for minimalism Sqlite is used as database

Some assumptions:
1. Order must be created first and should exist while payment is made
2. Payment payload takes "order_id" as required field to validate order before making payment
3. Response for payment is stored against the same order
4. For reference, payload can be found at test_PaymentGatewayNAMO.py file.

### db setup:
    run -> python manage.py db init
    run -> python manage.py db migrate
    run -> python manage.py db upgrade

### run tests:
    run ->python test_PaymentGatewayNAMO.py

### run app:
    create virtual environment
    run -> pip install -r requirements.txt
    create db
    run ->python manage.py runserver