import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            logger.error("Binance API keys not found. Check .env file.")
            self.client = None
        else:
            try:
                self.client = Client(
                    self.api_key,
                    self.api_secret,
                    testnet=True
                )
                self.client.FUTURES_URL = "https://testnet.binancefuture.com"
                logger.info("Binance client initialized (testnet).")
            except Exception as e:
                logger.exception("Failed to initialize Binance client.")
                self.client = None

    def is_ready(self):
        return self.client is not None
