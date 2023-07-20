import requests
from datetime import datetime
from twilio.rest import Client


END = "https://api.sunrise-sunset.org/json"
LAT = 19.075983
LON = 72.877655

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(iss_position)

    # checking the position of iss
    if LAT-5 <= latitude <= LAT+5 and LON-5 <= longitude <= LON+5:
        return True


def night():
    para = {
        "lat": LAT,
        "lon": LON,
        "formatted": 0
    }
    response = requests.get(END, params=para)
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


if night() and iss_overhead():
    account_sid = 'ACCOUNT SID'
    auth_token = 'TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='ISS is Overhead. Go outside.',
        to='YOUR WHATSAPP NUMBER'
    )
