import requests
from twilio.rest import Client



END = "https://api.openweathermap.org/data/2.5/weather"
api_key = "YOUR_API_KEY"
account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"

para ={
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key
}

response = requests.get(END, params=para)
# print(response.status_code)
response.raise_for_status()
data = response.json()
data_id = data["weather"][0]["id"]
if data_id < 800:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's gonna rain. Bring your umbrella ☔️.",
        to='YOUR_WHATSAPP_NUMBER'
    )
    # print(message.sid)
    print(message.status)
