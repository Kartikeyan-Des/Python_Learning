from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found")

city = input("Enter city name: ") 

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
elif response.status_code == 404:
    print(f"City '{city}' not found. Check the spelling.")
elif response.status_code == 401:
    print("Invalid API key. Check your .env file.")
else:
    print("Error:", response.status_code, response.text)