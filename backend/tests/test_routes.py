from app import create_app

def test_booking_route(client):
    """Test the bike booking API route."""
    app = create_app()
    client = app.test_client()

    response = client.post('/book', json={
        "user_id": 1,
        "amount": 20.0
    })

    assert response.status_code == 200
    assert response.json['status'] == 'success', "Booking route failed"
