import os
import csv
os.environ['SSLKEYLOGFILE'] = ''

import requests

with open("ajax-movies.csv","w",newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Movie Title", "Year", "Awards", "Nominations","Best-Pictire"])


    for year_num in range(1,6):
        url = f"https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=201{year_num}"

        response = requests.get(url)
        data = response.json()

        for movie in data:
            writer.writerow([
                        movie.get('title', ''),
                        movie.get('year', ''),
                        movie.get('awards', 0),
                        movie.get('nominations', 0),
                        movie.get('best_picture', False)
                        ])

print("Ajax movies .csv file saved...")