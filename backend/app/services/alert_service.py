# app/services/alert_service.py

def send_notification(user_id, message):
    """Send notification to user."""
    # In a real-world scenario, you'd connect to a WebSocket or push notification service.
    # For now, it prints to the console.
    print(f"Sending notification to user {user_id}: {message}")

    # You can also simulate notification storage here if needed
    return {"status": "success", "user_id": user_id, "message": message}
