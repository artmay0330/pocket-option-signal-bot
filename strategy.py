def get_signal():
    """
    This function will eventually contain the real trading strategy.

    For now, it returns a test signal.
    """

    signal = {
        "asset": "EUR/USD OTC",
        "direction": "BUY",
        "expiration": "1 Minute",
        "entry": "Enter now",
        "risk": "Low",
        "confidence": 92,
        "strategy": "Fib Pullback v1",
    }

    return signal
