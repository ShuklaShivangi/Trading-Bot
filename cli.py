import argparse
import sys

from bot.client import BinanceClient
from bot.orders import validate_order
from bot.utils import setup_logger


def main():
    logger = setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()
    logger.info(
    f"Received order request | Type={args.type}, Symbol={args.symbol}, Side={args.side}, Qty={args.quantity}, Price={args.price}")

    try:
        validate_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
        logger.info("Input validation successful.")
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        sys.exit(1)

    client_wrapper = BinanceClient()

    if not client_wrapper.is_ready():
        logger.error("Binance client is not ready. API keys missing or invalid.")
        print("Binance client not ready. Check API keys or KYC restrictions.")
        sys.exit(1)

    logger.info("Binance client is ready.")
    print("Binance client initialized successfully.")

    from bot.orders import place_market_order, place_limit_order

    if args.type == "MARKET":
        result = place_market_order(
        client=client_wrapper.client,
        symbol=args.symbol,
        side=args.side,
        quantity=args.quantity,
        logger=logger,
    )

    elif args.type == "LIMIT":
        result = place_limit_order(
        client=client_wrapper.client,
        symbol=args.symbol,
        side=args.side,
        quantity=args.quantity,
        price=args.price,
        logger=logger,
    )
    else:
        result = None

    if result:
        print(f"{args.type} order placed successfully.")
    else:
        print(f"{args.type} order failed. Check logs for details.")

if __name__ == "__main__":
    main()

