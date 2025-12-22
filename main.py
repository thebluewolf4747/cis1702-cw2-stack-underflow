import requests

API_URL = "https://restcountries.com/v3.1/name/"
COUNTRY_NAME = "france"
TIMEOUT = 10

try:
    response = requests.get(API_URL + COUNTRY_NAME, timeout=TIMEOUT)
    response.raise_for_status()
    print(response.status_code)
except requests.exceptions.RequestException:
    print("Failed to connect to API")
