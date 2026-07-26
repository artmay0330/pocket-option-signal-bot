REQUIRED_FIELDS = {
    "asset",
    "direction",
    "expiration",
    "entry",
    "risk",
    "confidence",
    "strategy",
}


def validate_signal(signal):
    if signal is None:
        return None

    if not isinstance(signal, dict):
        raise ValueError("Signal must be a dictionary or None.")

    missing_fields = REQUIRED_FIELDS - signal.keys()

    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"Signal is missing: {missing}")

    signal["direction"] = str(signal["direction"]).upper()

    if signal["direction"] not in {"BUY", "SELL"}:
        raise ValueError("Direction must be BUY or SELL.")

    signal["confidence"] = int(signal["confidence"])

    if not 0 <= signal["confidence"] <= 100:
        raise ValueError("Confidence must be between 0 and 100.")

    return signal
