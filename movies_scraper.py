import os
os.environ['SSLKEYLOGFILE'] = ''

import requests
import csv
from bs4 import BeautifulSoup

with open("movies.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title", "Worldwide Grossing", "Year"])

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films", headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, "html.parser")

    table1 = soup.find("table", class_="wikitable")
    rows = table1.find_all("tr")

    for row in rows[1:]:

        title = row.find("th").find("a").text.strip()

        cells = row.find_all("td")
        gross = cells[2].text.strip()
        year = cells[3].text.strip()
        
        writer.writerow([title, gross, year])


print("movies.csv created and saved succusesfully")