def validate_order(symbol, side, order_type, quantity, price=None):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and (price is None or price <= 0):
        raise ValueError("Price must be provided for LIMIT orders")
