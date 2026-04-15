import os
os.environ['SSLKEYLOGFILE'] = ''

import requests
import csv
from bs4 import BeautifulSoup

url = "https://scrapethissite.com/pages/forms/"
response = requests.get(url)

print(response.status_code)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

teams = soup.find_all("tr",class_="team")

for team in teams:
    name = team.find("td",class_="name").text.strip()
    Year = team.find("td",class_="year").text.strip()
    Wins = team.find("td",class_="wins").text.strip()
    Losses =team.find("td",class_="losses").text.strip()
    print(name, " | ", Year, " | ", Wins, " | ", Losses)
