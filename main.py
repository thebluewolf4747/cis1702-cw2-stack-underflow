import requests

API_URL = "https://restcountries.com/v3.1/name/"
TIMEOUT = 10


def get_country_info(country_name):
    try:
        response = requests.get(API_URL + country_name, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        country = data[0]

        name = country["name"]["common"]
        population = country["population"]
        region = country["region"]

        return {
            "name": name,
            "region": region,
            "population": population
        }

    except requests.exceptions.RequestException:
        return None


def main():
    country_info = get_country_info("france")

    if country_info is None:
        print("Failed to connect to API")
    else:
        print("Country:", country_info["name"])
        print("Region:", country_info["region"])
        print("Population:", country_info["population"])


main()
