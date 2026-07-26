import os

import requests


BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

MESSAGE = """
🚨 BINARY OPTIONS SIGNAL

Asset: EUR/USD OTC
Direction: BUY 🟢
Expiration: 1 Minute
Entry: Enter now

⚠️ Test signal only
""".strip()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": MESSAGE,
    },
    timeout=20,
)

response.raise_for_status()

print("Signal sent successfully.")
