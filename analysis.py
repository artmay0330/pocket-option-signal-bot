from market import get_market_data


def analyze_market():
    """
    Converts market data into a trading signal.

    Later this will contain your complete strategy.
    """

    market = get_market_data()

    if market["trend"] == "UP":
        direction = "BUY"
    else:
        direction = "SELL"

    return {
        "asset": "EUR/USD OTC",
        "direction": direction,
        "expiration": "1 Minute",
        "entry": "Enter now",
        "risk": "Low",
        "confidence": market["strength"],
        "strategy": "Fib Pullback v1",
    }
