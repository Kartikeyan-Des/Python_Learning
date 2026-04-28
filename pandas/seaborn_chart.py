import seaborn as sns
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
import requests
import matplotlib.pyplot as plt

load_dotenv() 
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found")
weather_data = []

cities = ["Chennai", "Mumbai", "Delhi", "Hyderabad"]

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_data.append({
        "City":city,
        "Temperature":data["main"]["temp"],
        "Feels_Like":data["main"]["feels_like"],
        "Humidity" : data["main"]["humidity"],
        "Weather" : data["weather"][0]["description"]
    })

df = pd.DataFrame(weather_data)
# print(data)
print(df)
# print("=========")
# print(df.sort_values("Temperature", ascending=False))
# print("=========")
# print(df[df["Humidity"] > 75])
# print(df.sort_values("Feels Like", ascending=False))

sns.heatmap(df[["Temperature", "Feels_Like", "Humidity"]].corr(), annot=True)
plt.title("Weather Correlation")
plt.show()

sns.pairplot(df[["Temperature", "Feels_Like", "Humidity"]])
plt.show()