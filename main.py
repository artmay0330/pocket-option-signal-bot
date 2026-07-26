import os
from datetime import datetime, timezone

import requests


# =========================
# TELEGRAM CONFIGURATION
# =========================

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


# =========================
# SIGNAL CONFIGURATION
# =========================

ASSET = "EUR/USD OTC"
DIRECTION = "BUY"
EXPIRATION = "1 Minute"
ENTRY = "Enter now"
RISK = "Low"
CONFIDENCE = 92
STRATEGY = "Fib Pullback v1"
TEST_MODE = True


# =========================
# TELEGRAM FUNCTION
# =========================

def send_signal(
    asset,
    direction,
    expiration,
    entry,
    risk,
    confidence,
    strategy,
):
    direction = direction.upper()

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

Asset: {asset}
Direction: {direction} {direction_icon}
Expiration: {expiration}
Entry: {entry}
Risk: {risk}
Confidence: {confidence}%
Strategy: {strategy}
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

send_signal(
    asset=ASSET,
    direction=DIRECTION,
    expiration=EXPIRATION,
    entry=ENTRY,
    risk=RISK,
    confidence=CONFIDENCE,
    strategy=STRATEGY,
)
