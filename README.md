# Stack Underflow - REST Countries Analyser

## Introduction
API Data Analyser using the REST countries API to give information on country population data.

## System Design
### Pseudocode
    SET API_URL to "https://restcountries.com/v3.1/name/"
    SET COUNTRY_NAME to "france"
    SET TIMEOUT to 10
    
    TRY
        SEND HTTP GET request to API_URL + COUNTRY_NAME with TIMEOUT
    
        IF response status is not successful
            THROW request error
    
        PARSE response as JSON and store in data
    
        IF data is empty
            PRINT "No country data found"
            SET data to null
        ELSE
            SET country to first item in data
    
            SET name to country["name"]["common"]
            SET population to country["population"]
            SET region to country["region"]
    
            PRINT "Country:", name
            PRINT "Region:", region
            PRINT "Population:", population
    
    CATCH any request error
        PRINT "Failed to connect to API"
        SET data to null

### Pseudocode - Parse data function
    FUNCTION parse_data(country)
        return {
            country_name,
            country_official_name,
            country_population,
            country_region,
            country_subregion,
            country_capital,
            country_currencies
        }

    INPUT country
    country_data = parse_data(country)

### Pseudocode - save counrty data to text file 
    Function save_to_file(parsed_country_data)

        Open "countries.txt" in append mode

        WRITE country namr to file
        WRITE official name to file
        WRITE region to file
        WRITE population to file
        WRITE borders to file 

        WRITE newline 
        CLOSE file
    END FUNCTION 
### Pseudocode - integration with main program 
    CALL get_country_info(COUNTRY_NAME)

    IF country data is null
        PRINT"Failed to connect to API"
    ELSE 
        CALL parse_data(country data)
        store result in parased_data

        CALL save_to_file(parased_data)

        PRINT parased_data 
    END IF 

## Pseudocode - Output to terminal
    FUNCTION report (country_data)
	    PRINT f"""
	    Report:
    Country name: (NAME)
    Population: (POPULATION)
    Region: (REGION)
    Borders: (BORDERS)
    """

## Data Anaylsis 

	FUNCTION calculate_population_stats(countries_data)
    	INPUT: List of country data objects
    	OUTPUT: Object with population statistics
    	IF countries_data is empty THEN
        	RETURN null
    	END IF
    	SET total_pop = 0
    	SET max_pop = 0
    	SET min_pop = very large number
    	SET max_country = null
    	SET min_country = null
    	FOR EACH country IN countries_data
        	ADD country.population TO total_pop
        	IF country.population > max_pop THEN
            	SET max_pop = country.population
            	SET max_country = country
        	END IF
        	IF country.population < min_pop THEN
            	SET min_pop = country.population
            	SET min_country = country
        	END IF
    	END FOR
    	SET avg_pop = total_pop / LENGTH(countries_data)
    	RETURN {
        	total_population: total_pop,
        	average_population: avg_pop,
        	most_populous: max_country,
        	least_populous: min_country
    	}
	END FUNCTION

	FUNCTION group_by_region(countries_data)
    	INPUT: List of country data objects
    	OUTPUT: Dictionary with regions as key
    	SET region_groups = empty dictionary
    	FOR EACH country IN countries_data
        	SET region = country.region
        	IF region NOT IN region_groups THEN
            	region_groups[region] = empty list
        	END IF
        	APPEND country TO region_groups[region]
    	END FOR
    	RETURN region_groups
	END FUNCTION

	FUNCTION compare_countries(country1, country2)
    	INPUT: Two country data objects
    	OUTPUT: Comparison object
    	SET pop_ratio = country1.population / country2.population
    	RETURN {
        	country1_name: country1.name,
        	country2_name: country2.name,
        	population_ratio: pop_ratio
			{
	END FUNCTION

## Implementation Summary
This application is an API data analyser using the REST Countries API that returns data about a country's population, region, and a country comparison. The program sends structured requests to the API, receives data in JSON format, and parses the response to extract relevant attributes such as population size and regional grouping.

After being extracted, the data is formatted into a clear, readable terminal output. The analyser presents the selected country's name, population, and region in a structured layout to improve usability and readability. A comparison feature is also implemented, allowing the population of two countries to be analysed side-by-side.

Finally, the data is saved to a text file for permanent storage.

## Testing
### Test data for saving functions
    TEST using vaild country name
        EXPECT data to be printed 
        EXPECT data to be saved in text file
    TEST using invalid country name
        EXPECT error message 
        EXPECT no data saved

## Contribution Breakdown

## Reflection

## Conclusion
