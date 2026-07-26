import os
from datetime import datetime, timezone

import requests

from config import TEST_MODE
from strategy import get_signal


BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


def send_signal(signal):
    direction = signal["direction"]
    direction_icon = "🟢" if direction == "BUY" else "🔴"

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


def main():
    signal = get_signal()

    if signal is None:
        print("No valid signal. Nothing was sent.")
        return

    send_signal(signal)


if __name__ == "__main__":
    main()
