# app/dynamic_pricing.py

def calculate_price(demand):
    """Calculate price based on predicted demand."""
    base_price = 5.0  # Base price for low demand
    if demand > 80:  # If predicted demand is high, apply surge pricing
        return base_price * 1.5  # Surge pricing for high demand
    elif demand > 50:  # If predicted demand is medium, apply medium pricing
        return base_price * 1.2
    return base_price  # Base price for low demand
