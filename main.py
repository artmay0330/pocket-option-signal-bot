import requests

BOT_TOKEN = "8312797274:AAG_NZ6qNgENzOgwNm1e3Sn8uYLeDhrj3Sg"
CHAT_ID = "-1004300871453""

message = "TEST SIGNAL"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
