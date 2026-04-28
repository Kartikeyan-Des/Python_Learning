import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.thehindu.com/news/national/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

headlines = soup.find_all("h3", class_="title")

headline_list = []

for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        headline_list.append({"Headline" : text})

df = pd.DataFrame(headline_list)
df["Headline_length"] = df['Headline'].str.len()
print(df.sort_values("Headline_length", ascending=False))
print(f"\nTotal headlines scraped: {len(df)}")


plt.plot(df.index, df["Headline_length"])
plt.xlabel("Headline Index")
plt.ylabel("Character Count")  
plt.title("Hindu Headlines Length")
plt.show()

plt.bar(df.index, df["Headline_length"])
plt.title("Bar Chart")
plt.show()

plt.hist(df["Headline_length"], bins=10)
plt.title("Histogram")
plt.show()

