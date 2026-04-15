import os
os.environ['SSLKEYLOGFILE'] = ''

import requests
import csv
from bs4 import BeautifulSoup

with open("hockey.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)   
    writer.writerow(["Team Name", "Year", "Wins", "Losses"])

    for i in range(1,25):
        url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")
        teams = soup.find_all("tr",class_="team")

        for team in teams:
            Name = team.find("td",class_="name").text.strip()
            Year = team.find("td",class_="year").text.strip()
            Wins = team.find("td",class_="wins").text.strip()
            Losses =team.find("td",class_="losses").text.strip()
            writer.writerow([Name, Year, Wins, Losses])

        print(f"page {i} saved")

print("Hockey.csv saves succesfully")