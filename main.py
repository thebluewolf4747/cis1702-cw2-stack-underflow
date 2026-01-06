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
        return data[0] if data else None
    
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
            "name": country["name"]["common"],
            "population": country["population"],
            "region": country["region"]
        }
        return parsed
    
    except (KeyError, TypeError) as e:
        print(f"Error during parse: {e}")
        return None

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
        print(f"""
Here is a report of the parsed data for that country:
Country: {report_data['name']}
Population: {report_data['population']}
Region: {report_data['region']}
        """)
    
    except KeyError as e:
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
    except KeyError as e:
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
    except (KeyError, IOError) as e:
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

def main():
    """
    Main function to execute the program.

    Returns:
    None

    """

    while True:
        try:
            print("Welcome to the Data Analyser! This program fetches data of countries " \
            "from the REST Countries API. Additionally, it can compare population statistics between countries. " \
            "Input a country to get started.")
            user_input1 = input("Enter the name of the country you want to fetch information for (press Enter to exit): ")
            if user_input1.strip() == "":
                break
            
            if type(user_input1) != str:
                print("Error: Please enter a valid country name (non-empty string).")
                continue
            
            country_data = get_country_info(user_input1)
            if country_data is None:
                print("Error: Could not fetch data for that country. Please try again.")
                continue
            
            parsed_data = parse_data(country_data)
            if parsed_data is None:
                print("Error: Could not parse country data. Please try again.")
                continue
            
            report_generic(parsed_data)
            save_country_to_file(parsed_data)
            
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        
        countries = [parsed_data]
        country_names = [user_input1]
        
        while True:
            try:
                country = input("Enter another country to compare (press Enter to exit to the first loop): ")
                
                if country.strip() == "":
                    break
                
                country_data = get_country_info(country)
                if country_data is None:
                    print("Error: Could not fetch data for that country. Please try again.")
                    continue
                
                parsed = parse_data(country_data)
                if not parsed:
                    continue
                
                report_generic(parsed)
                save_country_to_file(parsed)
                countries.append(parsed)
                country_names.append(country)
                
                stats = calculate_population_stats(countries)
                if stats:
                    report_population_stats(stats, country_names)
        
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue

if __name__ == "__main__":
    main()
