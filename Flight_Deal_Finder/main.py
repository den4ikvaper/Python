# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

import requests
from datetime import datetime, timedelta

SHEETY_ENDPOINT = "https://api.sheety.co/0d9244d7e0c9718a2981e99f34ff17a6/flightDeals/prices"
TEQUILA_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "DRQ8Bc3d__RVnzQ3466Z9zWoXuld1Jb5"

tequila_header = {
    "apikey": TEQUILA_API_KEY,
}

response = requests.get(SHEETY_ENDPOINT)
sheet_data = response.json()
# print(sheet_data['prices'])

for row in sheet_data['prices']:
    if len(row['iataCode'].strip()) == 0:
        # Find iataCode code of city from tequila and put it into variable
        tequila_params = {
            "term": row['city'],
            "location_types": "city"
        }
        replace_city = requests.get(TEQUILA_LOCATIONS_ENDPOINT, params=tequila_params,
                                    headers=tequila_header)
        new_city_code = replace_city.json()['locations'][0]['code']
        # Replace iataCode of city in spreadsheets
        new_iatacode = {
            "price": {
                'iataCode': new_city_code,
            }
        }
        change_iatacode = requests.put(f"{SHEETY_ENDPOINT}/{row['id']}", json=new_iatacode)

# Set dates
date_today = datetime.now() + timedelta(days=1)
date_from = date_today.strftime("%d/%m/%Y")
date_to = (date_today + timedelta(days=180)).strftime("%d/%m/%Y")

for row in sheet_data['prices']:
    # Search low price for each direction
    search_params = {
        "fly_from": "LON",
        "fly_to": row["iataCode"],
        "dateFrom": date_from,
        "dateTo": date_to,
        "curr": "GBP",
        "max_stopovers": "0",
        "flight_type": "round",
        "nights_in_dst_from": "7",
        "nights_in_dst_to": "28",
    }

    # Replace low price for each direction in spreadsheets
    search_response = requests.get(TEQUILA_SEARCH_ENDPOINT, params=search_params, headers=tequila_header)
    lowest_price = search_response.json()['data'][0]['price']

    new_lowest_price = {
        "price": {
            'lowestPrice': lowest_price,
        }
    }
    change_lowest_price = requests.put(f"{SHEETY_ENDPOINT}/{row['id']}", json=new_lowest_price)

    print(f"{row['city']}: £{lowest_price}")
