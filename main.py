import os
import requests
from dotenv import load_dotenv

load_dotenv("api_key.env")

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
URL = "https://www.alphavantage.co/query"

TIMEOUT = int(os.getenv("API_TIMEOUT", 10))

if not API_KEY:
    raise ValueError("ALPHA_VANTAGE_API_KEY not found in environment variables")

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": os.getenv("DEFAULT_SYMBOL", "AAPL"),
    "apikey": API_KEY
}

try:
    response = requests.get(URL, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    
    if "Error Message" in data:
        print("API Error:", data["Error Message"])
        data = None
    elif "Note" in data:
        print("Note:", data["Note"])
        
except requests.exceptions.RequestException as e:
    print("Error fetching data from API:", e)
    data = None

print(data)