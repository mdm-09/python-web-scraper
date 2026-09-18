import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    with open("my_first_data.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Added 'Rating' column to the header
        writer.writerow(["Title", "Price", "Rating"])

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            
            # Extracting the star rating class name (e.g., "Three", "Four")
            rating_p = book.find("p", class_="star-rating")
            rating = rating_p["class"][1] if rating_p else "N/A"

            writer.writerow([title, price, rating])

    print("Updated CSV generated with Ratings!")
else:
    print("Error:", response.status_code)