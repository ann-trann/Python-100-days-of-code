import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "2317f98c5d6d451e449410edab8e87d4"
account_sid = "AC685c9b64da19f630ae8b104412c54507"
auth_token = "fe02b9055967459f221afad94f7a578a"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# print(weather_data["hourly"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_="+12512765587",
            to="+84394668442"
        )
    print(message.status)

# client = Client(account_sid, auth_token)
# message = client.messages \
#     .create(
#     body="Keep learning Python and you'll soon know what it is.🍵",
#     from_="+12512765587",
#     to="+84394668442"
# )
# print(message.status)
