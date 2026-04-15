import os
os.environ['SSLKEYLOGFILE'] = ''

import requests
from bs4 import BeautifulSoup
import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])

    for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            writer.writerow([title, price, rating])

        print(f"Page {page} scraped!")

print("All done! Data saved to books.csv!")