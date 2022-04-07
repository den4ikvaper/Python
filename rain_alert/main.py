import requests
from twilio.rest import Client

account_sid = 'AC9312ddefb2f5a2e02275a4a3551dbdef'
auth_token = '24da38823f11a62d87c0232d16ba4331'
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "70e5793f6523a2218a96c33ea6a0dd42"

weather_params = {
    "lat": -8.839988,
    "lon": 13.289437,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages \
    .create(
    body="It's going to rain today. Remember to bring an ☔️ umbrella.",
    from_='+16202071026',
    to='+380989725981'
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body="It's don't going to rain today. Don't bring an ☔️ umbrella.",
        from_='+16202071026',
        to='+380989725981'
    )
    print(message.status)






