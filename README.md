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

## Implementation Summary

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
