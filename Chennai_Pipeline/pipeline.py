import sqlite3
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
load_dotenv()
API_KEY = os.getenv("API_KEY")
city = "Chennai"
time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
weather_data = []

if not API_KEY:
    raise ValueError("API_KEY not found")

def init_db():
    conn = sqlite3.connect("chennai_data.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblWeather(
                   ID INTEGER Primary key AUTOINCREMENT,
                   City Text,
                   Temperature Real,
                   Feels_Like Real,
                   Humidity INTEGER,
                   Weather Text,
                   Timestamp TEXT
                   )
    ''')
    conn.commit()
    return conn
conn = init_db()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

weather_data.append({
    "city":city,
    "Temperature":data["main"]["temp"],
    "Feels_Like": data["main"]["feels_like"],
    "Humidity": data["main"]["humidity"],
    "Weather": data["weather"][0]["description"],
    "Timestamp": time
})
df = pd.DataFrame(weather_data)

df.to_sql("tblWeather", conn, if_exists="append", index=False)
print(df)