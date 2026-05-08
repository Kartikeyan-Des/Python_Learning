import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("chennai_data.db")
df_weather = pd.read_sql("SELECT * FROM tblWeather", conn)
df_gold = pd.read_sql("SELECT * FROM tblGold", conn)

# print(df_weather)
# print("================")
# print(df_gold)


latest = df_weather.iloc[-1]
print(f"Current Temperature: {latest['Temperature']}°C")
print(f"Current Humidity: {latest['Humidity']}%")

print(f"Average Temperature: {df_weather['Temperature'].mean():.2f}°C")

print(f"Highest Temperature: {df_weather['Temperature'].max()}°C")

print(f"Lowest Temperature: {df_weather['Temperature'].min()}°C")



latestG = df_gold.iloc[-1]
print(f"Current Gold Price: {latestG['price']}₹")

print(f"Average Gold Price: {df_gold['price'].mean():.2f}₹")

print(f"Highest Gold Price: {df_gold['price'].max()}₹")

firstprice = df_gold.iloc[0]
print(f"First Gold Price: {firstprice['price']}₹")

lastprice = df_gold.iloc[-1]
print(f"Latest Gold Price: {lastprice['price']}₹")

change = firstprice['price'] - lastprice['price']
print(f"Gold Price Change: {change:.2f}₹")

print(f"Weather count in chennai: {df_weather['Weather'].value_counts()}")

sns.heatmap(df_weather[['Temperature', 'Humidity']].corr(), annot=True)
plt.title("Weather Correlation")
plt.show()