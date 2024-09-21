# app/services/payment_service.py

def process_payment(user_id, amount):
    """
    Simulate processing a payment for a user.
    
    Parameters:
    - user_id: ID of the user making the payment.
    - amount: Amount to be charged.

    Returns:
    - A dictionary with payment status and details.
    """
    # This is a mock function, in a real-world scenario you'd call an external payment gateway
    if amount <= 0:
        return {"status": "failed", "message": "Invalid payment amount."}

    # Simulate a successful payment process
    return {"status": "success", "user_id": user_id, "amount": amount, "message": "Payment processed successfully."}
