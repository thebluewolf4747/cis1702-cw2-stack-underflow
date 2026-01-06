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
    
    except requests.exceptions.RequestException as e:
        # Handles API-related errors
        print(f"Request error occurred: {e}")
        return None

    except Exception as e:
        # Handles all errors
        print(f"Error occurred while fetching country data: {e}")
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
            raise ValueError("No valid country data provided.")
        
        # Key fields
        country_name = country["name"]["common"]
        population = country["population"]
        region = country["region"]

        parsed = {
            "name": country_name,
            "population": population,
            "region": region
        }

    except (KeyError, TypeError, ValueError) as e:
        # Handles parsing errors
        print(f"Error during parse: {e}")

    else:
        return parsed
    
def report_generic(report_data):
    """
    Reports the parsed data and statistics.

    Parameters:
    report_data (dict): Parsed country data.
    population_stats (dict): Population statistics.
    comparison (dict): Comparison between two countries.

    Returns:
    None (prints the output).

    """
    try:
        print (f"""
Here is a report of the parsed data for that country:
Country: {report_data['name']}
Population: {report_data['population']}
Region: {report_data['region']}
        """)
    
    except Exception as e:
        print(f"Error during report generation: {e}")

def report_population_stats(population_stats, countries_list):
    try:
        print(f"""
Here are the population statistics for the given countries {countries_list}:
Total population: {population_stats['total_population']}
Average population: {population_stats['average_population']}
Most populous country population: {population_stats['most_populous']}
Least populous country population: {population_stats['least_populous']}
        """)

    except Exception as e:
        print(f"Error during report generation: {e}")


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

    try:
        with open("countries.txt", "a") as file:
            file.write(
                f"Country: {country_data['name']}, "
                f"Population: {country_data['population']}, "
                f"Region: {country_data['region']}\n"
            )

    except IOError as e:
        print(f"Error writing to file: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
    
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
    avg_pop = 0
    max_pop = None
    populations = []


    try:
        for country in countries_data:
            population = country.get("population", 0)
            total_pop += population
            populations.append(population)
            
        max_pop = max(populations)
        min_pop = min(populations)

        avg_pop = total_pop / len(countries_data)
    
    except Exception as e:
        print(f"Error calculating population statistics: {e}")
        return None

    return {
        "total_population": total_pop,
        "average_population": avg_pop,
        "most_populous": max_pop,
        "least_populous": min_pop
    }

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
    
    try:
        country_data = get_country_info(country_name)

        if country_data is None:
            raise ValueError("Failed to connect to API")

        parsed_data = parse_data(country_data)
        
        if parsed_data is None:
            raise ValueError("Failed to parse country data")
        
        save_country_to_file(parsed_data)

    except ValueError as e:
        print(f"Value error: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected error during integration: {e}")
        return None
    
    else:
        return parsed_data
        
def main():
    """
    Main function to execute the program.

    Returns:
    None

    """

    while True:
        try:
            user_input1 = input("Enter the name of the country you want to fetch information for: ")
            if user_input1 is None or type(user_input1) != str:
                raise ValueError("Invalid country name provided.")
            
            if user_input1.lower() == "":
                print("Try again: Cannot accept an empty string")
                continue

        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        
        try:
            country_data = get_country_info(user_input1) if user_input1 else None
            parsed_data = parse_data(country_data)
        
        except Exception as e:
            print(f"An error occurred while fetching country data: {e}")
            country_data = None
        
        try:
            country_names = [user_input1]
            
            while True:
                country = input("Enter a country if you would like to compare their statistics (Press Enter if not): ")
                country_names.append(country)

                if country.lower() == "":
                    country_names.pop()  # Remove the last empty entry
                    False
                    break
                
                if country is None or type(country) != str:
                    print("Invalid country name provided. Please try again.")
                    country_names.pop()  # Remove the invalid entry
                    continue
            
            countries = [get_country_info(country) for country in country_names]
            report_generic(parsed_data)
            report_population_stats(calculate_population_stats(countries), country_names)
            save_country_to_file(parsed_data)
            save_country_to_file(country for country in countries if country is not None or country != "")
        
        except Exception as e:
            print(f"An error occurred during reporting: {e}")

main()