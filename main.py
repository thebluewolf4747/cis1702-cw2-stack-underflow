import requests

API_URL = "https://restcountries.com/v3.1/name/"
COUNTRY_NAME = "france"
TIMEOUT = 10

try:
    response = requests.get(API_URL + COUNTRY_NAME, timeout=TIMEOUT)
    response.raise_for_status()

    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    population = country["population"]
    region = country["region"]

    print(name)
    print(population)
    print(region)

except requests.exceptions.RequestException:
    print("Failed to connect to API")
