# Stack Underflow - REST Countries Analyser

## Introduction
API Data Analyser using the REST countries API to give information on country population data.


## Pseudocode
LOAD environment variables from "api_key.env"

SET API_KEY to environment variable "ALPHA_VANTAGE_API_KEY"
SET API_URL to Alpha Vantage API endpoint
SET TIMEOUT to environment variable "API_TIMEOUT" or default to 10

IF API_KEY is missing
    THROW error "API key not found"

SET request parameters:
    function = "TIME_SERIES_DAILY"
    symbol = environment variable "DEFAULT_SYMBOL" or "AAPL"
    apikey = API_KEY

TRY
    SEND HTTP GET request to API_URL with parameters and TIMEOUT
    IF response status is not successful
        THROW request error

    PARSE response as JSON and store in data

    IF data contains "Error Message"
        PRINT API error message
        SET data to null
    ELSE IF data contains "Note"
        PRINT note message

CATCH any request error
    PRINT error message
    SET data to null

PRINT data
