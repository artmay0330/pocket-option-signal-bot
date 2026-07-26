import os
from datetime import datetime, timezone

import requests


BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

ASSET = "EUR/USD OTC"
DIRECTION = "BUY"
EXPIRATION = "1 Minute"
ENTRY = "Enter now"

direction_icon = "🟢" if DIRECTION.upper() == "BUY" else "🔴"

current_time = datetime.now(timezone.utc).strftime("%I:%M %p UTC")

message = f"""
🚨 BINARY OPTIONS SIGNAL

Asset: {ASSET}
Direction: {DIRECTION.upper()} {direction_icon}
Expiration: {EXPIRATION}
Entry: {ENTRY}
Time: {current_time}

⚠️ Test signal only
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
