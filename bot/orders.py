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
    
def place_market_order(client, symbol, side, quantity, logger):
    logger.info(
        f"Attempting MARKET order | Symbol={symbol}, Side={side}, Quantity={quantity}"
    )

    if client is None:
        logger.error("Binance client not initialized. Cannot place order.")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )
        logger.info(f"Market order placed successfully: {order}")
        return order

    except Exception as e:
        logger.exception("Failed to place MARKET order.")
        return None

def place_limit_order(client, symbol, side, quantity, price, logger):
    logger.info(
        f"Attempting LIMIT order | Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}"
    )

    if client is None:
        logger.error("Binance client not initialized. Cannot place LIMIT order.")
        return None

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )
        logger.info(f"Limit order placed successfully: {order}")
        return order

    except Exception as e:
        logger.exception("Failed to place LIMIT order.")
        return None
