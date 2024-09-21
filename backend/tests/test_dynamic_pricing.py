def test_dynamic_pricing():
    """Example test for dynamic pricing."""
    # Assume we have a pricing function
    def calculate_price(demand):
        base_price = 10
        if demand > 100:
            return base_price * 1.2  # Surge pricing
        return base_price
    
    # High demand, surge pricing
    assert calculate_price(150) == 12, "Dynamic pricing failed for high demand"
    
    # Low demand, no surge pricing
    assert calculate_price(80) == 10, "Dynamic pricing failed for low demand"
