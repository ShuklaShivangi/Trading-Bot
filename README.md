
# Binance Futures Trading Bot (Testnet)

## Overview
This project is a CLI-based trading bot built in Python that interacts with the Binance USDT-M Futures **Testnet**.
It allows users to place Market and Limit orders via command-line arguments with proper input validation,
structured logging, and safe error handling.

This project is designed for learning and evaluation purposes and does **not** place real trades.

---

## Features
- Command-line interface using `argparse`
- Supports **Market** and **Limit** orders
- Input validation for symbols, order type, quantity, and price
- Structured logging for requests, responses, and errors
- Graceful handling of missing API keys or restricted access
- Modular and reusable code structure

---

## Project Structure

```
Trading-Bot/
├── bot/
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ └── utils.py # Validation and logging utilities
├── cli.py # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/ShuklaShivangi/Trading-Bot.git
cd Trading-Bot
```
### 2. Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt

API Configuration (Testnet)

This project uses the Binance Futures Testnet.

Create a .env file in the root directory with:

BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```
### Note:
Binance currently requires Intermediate Identity Verification (KYC) to create API keys.
If API keys are unavailable, the application exits gracefully with clear logs.
This behavior is expected and handled intentionally.

### Usage Examples
Market Order
```python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01```

Limit Order
```python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000```

Logging

All actions, validations, and errors are logged with timestamps.
Logs help in debugging and tracing application flow.

Notes:

This project focuses on clean architecture, validation, and error handling.
Real trade execution is not performed without valid API credentials.
Designed as an evaluation assignment for backend Python roles.

Author

Shivangi Shukla


---

