def calculate_price(demand):
    """Calculate price based on predicted demand."""
    base_price = 5.0  # Base price for low demand
    if demand > 0.8:
        return base_price * 1.5  # Surge pricing for high demand
    elif demand > 0.5:
        return base_price * 1.2  # Medium pricing
    return base_price
