# Binance Futures Testnet Trading Bot

A simplified Python CLI trading bot built for Binance Futures Testnet (USDT-M).  
This application supports placing Market and Limit orders with BUY and SELL sides using Binance API.

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL
- Command-line interface using argparse
- Input validation
- Logging of requests, responses, and errors
- Exception handling for invalid input, API issues, and network errors

## Files

- `cli.py` - Main entry point
- `client.py` - Binance API client and order execution
- `validators.py` - Input validation logic
- `logging_config.py` - Logging setup
- `requirements.txt` - Dependencies

## Installation

```bash
git clone <your-repository-url>
cd binance-futures-testnet-bot

