import requests
from datetime import datetime

MY_LAT = 10.823099
MY_LONG = 106.629662

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
# print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":")[0])

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)

