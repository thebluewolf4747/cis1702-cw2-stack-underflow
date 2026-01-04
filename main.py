import requests

API_URL = "https://restcountries.com/v3.1/name/"
TIMEOUT = 10


def get_country_info(country_name):
    try:
        response = requests.get(API_URL + country_name, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        country = data[0]
        
        return country

    except requests.exceptions.RequestException:
        return None
    
def parse_data(country):
    country_name = country["name"]["common"]
    official_name = country["name"]["official"]
    population = country["population"]
    region = country["region"]
    borders = country["borders"]

    return {
        "name": country_name,
        "official_name": official_name,
        "population": population,
        "region": region,
        "borders": borders
    }

def report (report_data):
    print (f"""
Here is a report of the parsed data:
Country: {report_data['name']}
Population: {report_data['population']}
Region: {report_data['region']}
Borders: {report_data['borders']}
    """)

def main():
    country_data = get_country_info("france")
    parsed_data = parse_data(country_data)

    if country_data is None:
        print("Failed to connect to API")
    else:
        #print(parsed_data)
        report(parsed_data)
        #Changed this to call the report function if it breaks the code the original line is just commented out

main()

