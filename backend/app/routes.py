# app/routes.py
from flask import request, jsonify
from app.models import db

def setup_routes(app):
    @app.route('/book', methods=['POST'])
    def book_bike():
        # Import inside the function to avoid circular imports
        from app.services.payment_service import process_payment

        data = request.json
        user_id = data['user_id']
        amount = data['amount']

        # Call the payment service function
        payment_result = process_payment(user_id, amount)

        return jsonify(payment_result)
