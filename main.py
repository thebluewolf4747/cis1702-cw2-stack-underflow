import requests

API_URL = "https://restcountries.com/v3.1/name/"
COUNTRY_NAME = "france"

response = requests.get(API_URL + COUNTRY_NAME)

print(response.status_code)
