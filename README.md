# Stack Underflow - REST Countries Analyser

## Introduction
API Data Analysis  using the REST countries API to give information on country population data.
Project Documentation: API Data Analysis using REST Countries API
	
In today’s world, data drives decisions. Understanding country-specific statistics like population, region, and demographics is essential for businesses, 	researchers, and policymakers. The API Data Analysis project leverages the REST Countries API to fetch and analyse country information efficiently. By using a RESTful API, we can programmatically access up-to-date data about countries, process it, and generate meaningful insights.
1. Project Goal: 
The goal of this project was to develop a command-line tool that interacts with a public API, performs basic data analysis, and generates a report file. 	The project uses the REST Countries API to retrieve country data and provide meaningful insights into population, region, and borders.
The tool allows users to query a country by name, fetch data, analyse it, and store the results in a report file for future reference.
This project focuses on creating a tool that allows users to:

- Retrieve detailed country information
- Calculate population statistics
- Group countries by region
- Compare countries based on population

This serves as both an educational exercise in API handling and a practical tool for data analysis.

2. Objective: The main objective of this project is to provide a simple, interactive system to analyse country data in real-time using the REST Countries API.
Users can:
- Search for a country and retrieve information
- Save country data for future reference
- Compare populations between countries
- Generate statistical summaries of populations
- Group countries by region

This gives a structured way to work with real-world data while learning about API integration, data processing, and basic analytics.

3. Why This Project Was Chosen:
- APIs are a fundamental part of modern programming and software development.
- Country data is publicly available and provides a meaningful dataset for analysis.
- This project combines data retrieval, processing, and presentation, covering multiple essential skills in computer science.
- It introduces students to error handling, data parsing, storage, and analysis in a real-world scenario.

4. Advantages
- Real-Time Data: The API always provides updated information, making the tool reliable.
- Automation: Instead of manually searching country data, users can retrieve and process it programmatically.
- Scalability: The tool can easily be extended to include more statistics or visualizations.
- Educational Value: Helps users understand REST APIs, JSON parsing, and data analysis concepts.
- Reusable: Data saved in files allows for future processing without repeated API calls.

5. Disadvantages / Limitations
- API Dependency: If the REST Countries API is down or its endpoints change, the program may fail.
- Data Limitation: Only the data provided by the API is available; additional statistics may need external sources.
- Performance: Fetching data for many countries simultaneously could slow down the program.
- Error Handling: Users must handle exceptions, such as invalid country names or missing fields.

6. Future Applications - This project lays the foundation for multiple future enhancements:
- Data Visualization: Generate charts and graphs for population or regional analysis.
- Expanded Metrics: Include GDP, life expectancy, or literacy rate if APIs provide them.
- Web Interface: Turn the program into a web application for user-friendly access.
- Educational Tool: Teach students about geography, demographics, and API integration.
- Data Science Integration: Feed the retrieved data into machine learning models for predictive analysis.

7. How the Project Works
- Data Retrieval: The program fetches country data from the REST Countries API using HTTP requests.
- Parsing: Extracts essential information such as country name, population, region, and borders.
- Reporting: Generates a readable report of the parsed data for the user.
- Storage: Saves country data into a text file for future reference.
- Analysis: Calculates total, average, minimum, and maximum population, groups countries by region, and allows comparison between countries.


| Requirement                         | Implementation                                                                                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   Interact with a public JSON API   | The program fetches country data from the **REST Countries API** using Python’s `requests` library.                                                       |
|   User input query                  | Users can input a country name (e.g., `"France"`) which is used to fetch data from the API.                                                               |
|   Parse JSON response               | The JSON response is parsed to extract key information including country name, population, region, and borders                     						  |
|   Data Extraction                   | At least four key pieces of data are extracted: **name, population, region, borders**.                                                                    |
|   Simple Analysis                   | The program calculates **total, average, largest, and smallest populations**, compares populations between two countries, and groups countries by region. |
|   Display Output                    | A clean summary is printed to the console using a formatted **report function**.                                                                          |
|   Generate Report File              | The data is appended to a **`countries.txt`** file for record-keeping.                                                                                    |
|   Error Handling                    | Robust error handling is implemented with `try-except` blocks for network errors, invalid input, and missing fields in the JSON response.                 |              


## System Design
### Pseudocode - Fetch data
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
            country_population,
            country_region
        }

    INPUT country
    country_data = parse_data(country)

### Pseudocode - save country data to text file 
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
	FUNCTION report (country_data, population_stats, comparison_of_countries)
		OUTPUT
		Report:
		Name: COUNTRY NAME
		Population: POPULATION
		Region: REGION
	
		Stats about the population
		Total population: TOTAL POPULATION
		Average population: AVG POPULATION
	
		Comparison data between two countries:
		Country 1: COUNTRY 1 NAME
		Country 2: COUNTRY 2 NAME
		Population ratio: POPULATION RATIO
		END OUTPUT
	END FUNCTION 

## Pseudocode - Data Analysis 

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
Kim:
- Added pseudocode for his function with defensive coding features
- Converted this pseudocode into Python code

Rayyan:
- Added the parse data function to the code - this included the data to be analysed
- Worked on the implementation summary in the documentation
- Implemented robust error handling

Jack:
Added data analysis functions pseudocode to be implemented in Python by Joel:
- calculate_population_stats()
- group_by_region()
- compare_countries()

Neil:
- Added the pseudocode for the output of the analysed data
- Added the actual code for this function

Joel:
- Implemented Jack's pseudocode
- Added testing to documentation
- Added save function to pseudocode
- Implemented save function in Python

## Reflection
In summary, this project was a valuable learning experience that integrated multiple core programming concepts into a realistic application. By working with a real-world API, I was able to connect theory with practical programming, especially in terms of handling JSON data, making HTTP requests, and navigating unpredictable user input. Utilising the REST Countries API made the project feel truly relevant and meaningful, rather than just another program filled with hard-coded information.
A major takeaway for me was realizing the significance of error handling when working with external APIs. We faced some genuine issues, such as network failures, invalid country names, and missing fields, all of which had to be managed effectively to avoid crashes. By implementing defensive coding techniques and using try-except blocks, we were able to make the program much sturdier and easier for users. This experience reinforced the idea that real software should always be prepared for things to go wrong.
Teamwork played a major role in the success of the project. Splitting tasks such as API handling, data parsing, analysis, and documentation ensured that everyone contributed meaningfully. Translating pseudocode into working Python code showed how planning before coding saves time and reduces errors. Reviewing each other’s work also helped catch mistakes early and improve overall code quality.
That said, the project does have limitations. The program relies entirely on the REST Countries API, meaning changes to the API or downtime could break functionality. Performance could also become an issue if the tool were expanded to fetch data for many countries at once. However, these limitations helped highlight areas for future improvement, such as caching data locally, optimising requests, or expanding to additional APIs.

## Conclusion
