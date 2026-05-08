import sqlite3
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
load_dotenv()
API_KEY = os.getenv("API_KEY")
GOLD_API_KEY = os.getenv("GOLD_API_KEY")

city = "Chennai"
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
weather_data = []
gold_data = []

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

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblGold(
                   ID INTEGER Primary Key AUTOINCREMENT,
                   price DECIMAL,
                   high_price DECIMAL,
                   low_price DECIMAL,
                   open_price DECIMAL,
                   price_gram_22k DECIMAL,
                   timestamp TEXT
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


url = "https://www.goldapi.io/api/XAU/INR"
headers = {"x-access-token": GOLD_API_KEY}
response1 = requests.get(url, headers=headers)
data1 = response1.json()

gold_data.append({
    "price":data1['price'],
    "high_price":data1['high_price'],
    "low_price":data1['low_price'],
    "open_price":data1['open_price'],
    "price_gram_22k":data1['price_gram_22k'],
    "timestamp": datetime.fromtimestamp(data1['timestamp']).strftime("%Y-%m-%d %H:%M:%S")
})
df_gold = pd.DataFrame(gold_data)
df_gold.to_sql("tblGold", conn, if_exists="append", index=False)
print(df_gold)