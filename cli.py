import argparse
from bot.client import BinanceFuturesClient
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Example: BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Required for LIMIT order")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\nOrder Request Summary")
        print("----------------------")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")
        if price:
            print(f"Price    : {price}")

        client = BinanceFuturesClient()

        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\nOrder Placed Successfully ")
        print("----------------------------")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")

    except Exception as e:
        print(f"\nOrder Failed ❌ : {e}")


if __name__ == "__main__":
    main()