import os
from datetime import datetime, timezone

import requests

from strategy import get_signal


# =========================
# TELEGRAM CONFIGURATION
# =========================

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

TEST_MODE = True


# =========================
# TELEGRAM FUNCTION
# =========================

def send_signal(signal):
    direction = signal["direction"].upper()

    if direction == "BUY":
        direction_icon = "🟢"
    elif direction == "SELL":
        direction_icon = "🔴"
    else:
        raise ValueError("Direction must be BUY or SELL.")

    current_time = datetime.now(timezone.utc).strftime("%I:%M %p UTC")

    test_warning = "\n\n⚠️ Test signal only" if TEST_MODE else ""

    message = f"""
🚨 BINARY OPTIONS SIGNAL

Asset: {signal["asset"]}
Direction: {direction} {direction_icon}
Expiration: {signal["expiration"]}
Entry: {signal["entry"]}
Risk: {signal["risk"]}
Confidence: {signal["confidence"]}%
Strategy: {signal["strategy"]}
Time: {current_time}{test_warning}
""".strip()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message,
        },
        timeout=20,
    )

    response.raise_for_status()

    print("Signal sent successfully.")


# =========================
# RUN BOT
# =========================

signal = get_signal()
send_signal(signal)
