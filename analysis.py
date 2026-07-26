from config import ASSET, EXPIRATION, MINIMUM_CONFIDENCE
from market import get_market_data


def analyze_market():
    """
    Analyze market data and return either:
    - A completed signal dictionary
    - None when no valid setup exists
    """

    market = get_market_data()

    trend = market["trend"].upper()
    confidence = int(market["strength"])

    if confidence < MINIMUM_CONFIDENCE:
        return None

    if trend == "UP":
        direction = "BUY"
    elif trend == "DOWN":
        direction = "SELL"
    else:
        return None

    return {
        "asset": ASSET,
        "direction": direction,
        "expiration": EXPIRATION,
        "entry": "Enter now",
        "risk": "Low",
        "confidence": confidence,
        "strategy": "Trend Strength v1",
    }
