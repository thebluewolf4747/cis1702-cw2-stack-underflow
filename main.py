import requests

API_URL = "https://restcountries.com/v3.1/name/"
TIMEOUT = 10

def get_country_info(country_name):
    """ 
    Fetches country information from the REST Countries API.

    Parameters:
    country_name (str): The name of the country to fetch information for.

    Returns:
    dict: A dictionary containing country information if successful, None otherwise.

    """
    try:
        response = requests.get(API_URL + country_name, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        country = data[0]
        
        return country

    except requests.exceptions.RequestException:
        return None
    
def parse_data(country):
    """ 
    Parses country data to extract relevant information.
    
    Parameters:
    country (dict): The full JSON response as a dictionary of country data to parse.

    Returns:
    dict: A dictionary containing parsed country information.

    """
    parsed = None
    try:
        if country is None:
            raise ValueError("No country data provided.")
        
        country_name = country["name"]["common"]
        population = country["population"]
        region = country["region"]

    except (KeyError, TypeError, ValueError) as e:
        print(f"Error during parse: {e}")

    else:
        parsed = {
            "name": country_name,
            "population": population,
            "region": region
        }
    
    finally:
        print("Parsed data!")

    return parsed
    
def report (report_data, population_stats, comparison):
    """
    Reports the parsed data and statistics.

    Parameters:
    report_data (dict): Parsed country data.
    population_stats (dict): Population statistics.
    comparison (dict): Comparison between two countries.

    Returns:
    None (prints the output).

    """

    print (f"""
Here is a report of the parsed data:
Country: {report_data['name']}
Population: {report_data['population']}
Region: {report_data['region']}
    """)
    print(f"""
Here are the population statistics for {report_data['name']}:
Total population: {population_stats['total_population']}
Average population: {population_stats['average_population']}
          """)
    print(f"""
Here is the population ratio between two countries:
First country: {comparison['country1_name']}
Second country: {comparison['country2_name']}
Population ratio: {comparison['population_ratio']}
    """)

# save country data to text file 
def save_country_to_file(country_data):
    """
    Saves country data to a text file.

    Parameters:
    country_data (dict): Parsed country data.

    Returns:
    file object: The file object where data is saved.

    """
    if country_data is None:
        return

    with open("countries.txt", "a") as file:
        file.write(
            f"Country: {country_data['name']}, "
            f"Population: {country_data['population']}, "
            f"Region: {country_data['region']}\n"
        )

        return file
# calculate populaation statistics 
def calculate_population_stats(countries_data):
    """
    Calculates population statistics for a list of countries.
    
    Parameters:
    countries_data (list): A list of dictionaries containing country data.
    
    Returns:
    dict: A dictionary containing total, average, most populous, and least populous countries.

    """

    if not countries_data:
        return None

    total_pop = 0
    max_pop = 0
    min_pop = float("inf")

    max_country = None
    min_country = None

    for country in countries_data:
        population = country.get("population", 0)
        total_pop += population

        if population > max_pop:
            max_pop = population
            max_country = country

        if population < min_pop:
            min_pop = population
            min_country = country

    avg_pop = total_pop / len(countries_data)

    return {
        "total_population": total_pop,
        "average_population": avg_pop,
        "most_populous": max_country,
        "least_populous": min_country
    }

# group countries by region 
def group_by_region(countries_data):
    """
    Groups countries by their region.
    
    Parameters:
    countries_data (list): A list of dictionaries containing country data.
    
    Returns:
    dict: A dictionary with regions as keys and lists of countries as values.

    """

    region_groups = {}

    for country in countries_data:
        region = country.get("region", "Unknown")

        if region not in region_groups:
            region_groups[region] = []

        region_groups[region].append(country)

    return region_groups

# compare to countries 
def compare_countries(country1, country2):
    """
    Compares two countries based on their population.
    
    Parameters:
    country1 (dict): The first country's data.
    country2 (dict): The second country's data.
    
    Returns:
    dict: A dictionary containing the names of both countries and their population ratio.
    
    """
    
    pop1 = country1.get("population", 0)
    pop2 = country2.get("population", 1)

    return {
        "country1_name": country1.get("name"),
        "country2_name": country2.get("name"),
        "population_ratio": pop1 / pop2
    }

def integrate_and_store(country_name):
    """
    Integrates fetching, parsing, and storing country data.
    
    Parameters:
    country_name (str): The name of the country to process.
    
    Returns:
    dict: Parsed country data.
    
    """
    
    country_data = get_country_info(country_name)

    if country_data is None:
        print("Failed to connect to API")
        return None

    parsed_data = parse_data(country_data)
    save_country_to_file(parsed_data)

    return parsed_data

# testing systems 
def test_system():
    """
    Tests the integration and storage system.
    
    Returns:
    None
    
    """

    countries = []

    france = integrate_and_store("france")
    germany = integrate_and_store("germany")

    if france:
        countries.append(france)
    if germany:
        countries.append(germany)

    stats = calculate_population_stats(countries)
    print("Population Statistics:", stats)

    grouped = group_by_region(countries)
    print("Grouped by Region:", grouped)

    if len(countries) == 2:
        comparison = compare_countries(countries[0], countries[1])
        print("Country Comparison:", comparison)
        
def main():
    """
    Main function to execute the program.

    Returns:
    None

    """

    country_data = get_country_info("france")
    parsed_data = parse_data(country_data)
    comparison_data = {"country1_name": "france", "country2_name": "germany", "population_ratio": 1.5}

    if country_data is None:
        print("Failed to connect to API")
    else:
        report(parsed_data, calculate_population_stats([parsed_data]), comparison_data)
        test_system()

main()



