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
    if amount <= 0:
        return {"status": "failed", "message": "Invalid payment amount."}

    # Simulate successful payment
    print(f"Processing payment of ${amount} for user {user_id}.")
    return {"status": "success", "user_id": user_id, "amount": amount, "message": "Payment processed successfully."}

    # In a real-world scenario, you'd connect to a payment API, check for errors, etc.
