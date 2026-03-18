from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "lat": 13.0827,
    "lon": 80.2707,
    "appid": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)