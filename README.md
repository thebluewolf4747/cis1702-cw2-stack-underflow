# Stack Underflow - REST Countries Analyser

## Introduction
API Data Analyser using the REST countries API to give information on country population data.


## Pseudocode
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

