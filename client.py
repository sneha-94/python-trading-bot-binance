import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
import os

load_dotenv()


class BinanceFuturesClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.api_secret = os.getenv("API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found in .env file")

        self.client = Client(self.api_key, self.api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }

            if order_type.upper() == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            logging.info(f"Order Request: {params}")

            response = self.client.futures_create_order(**params)

            logging.info(f"Order Response: {response}")

            return response

        except BinanceAPIException as e:
            logging.error(f"Binance API Error: {e}")
            raise

        except BinanceRequestException as e:
            logging.error(f"Network Error: {e}")
            raise

        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            raise