import requests
import os

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/cf15e951620d40c82cdd92658ac08e2d/flightDeals/prices"
#os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
# print(SHEETY_PRICES_ENDPOINT)
TOKEN = os.environ.get("TOKEN")
# print(TOKEN)
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        print(data)
        pass
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data


