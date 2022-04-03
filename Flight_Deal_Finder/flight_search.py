import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "DRQ8Bc3d__RVnzQ3466Z9zWoXuld1Jb5"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(location_endpoint, params=query, headers=headers)
        result = response.json()['locations']
        code = result[0]['code']
        return code
