import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Virat_Kohli"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "infobox vcard"})

labels = []
values = []

for row in table.find_all("tr"):
    label = row.find("th")
    value = row.find("td")
    if label and value:
        labels.append(label.text.strip())
        values.append(value.text.strip())

data = dict(zip(labels, values))

# Write the data to a CSV file
with open("virat_kohli_info.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(["Attribute", "Value"])

    for label, value in data.items():
        csvwriter.writerow([label, value])

print("Data has been scraped and saved in 'virat_kohli_info.csv' file.")