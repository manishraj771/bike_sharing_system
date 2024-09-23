# app/routes.py
from flask import request, jsonify
from app.models import db

def setup_routes(app):

    @app.route('/book', methods=['POST'])
    def book_bike():
        # Import the process_payment service
        from app.services.payment_service import process_payment

        # Assume the request JSON contains user_id and payment amount
        data = request.json
        user_id = data.get('user_id')
        amount = data.get('amount')

        # Call the payment service to process the payment
        payment_result = process_payment(user_id, amount)

        # Handle the response from the payment service
        if payment_result['status'] == 'failed':
            return jsonify(payment_result), 400

        # Simulate bike booking logic after successful payment
        return jsonify({"status": "success", "message": "Bike booked successfully.", "payment_details": payment_result})
        
