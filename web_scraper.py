import pandas as pd
import requests
from bs4 import BeautifulSoup
import time


def scraper_cover_image(title):
    try:
        query = title.replace(" ", "+")
        url = f"https://openlibrary.org/search?q={query}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
        }

        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        bookcover = soup.find(class_="bookcover")
        img_tag = bookcover.find("img")
        image_source = img_tag.attrs["src"]
        image_source = "http:" + image_source

        response = requests.get(image_source)
        if response.status_code == 200:
            exstetnsion = image_source.split(".")[-1]
            file_name = f"{title.lower().replace(" ", "_")}.{exstetnsion}"
            with open(f"static/covers/{file_name}", "wb") as f:
                f.write(response.content)
                print(f"[INFO] Cover found for: {title} - {author}")
                return file_name
        else:
            print(f"[INFO] Cover not found: {title}")
            return None

    except Exception as e:
        print(f"[ERROR] Error scraping cover for book: {title}, error: {e}")
        return None


df = pd.read_csv("books.csv")

for index, row in df.iterrows():
    title = row["title"]
    author = row["author"]
    cover = row["cover"]

    if (pd.isna(cover)):
        print(f"[INFO] Searching book cover for: {title} - {author}...")

        image_title = scraper_cover_image(title)

        if image_title:
            df.at[index, "cover"] = image_title
            df.to_csv("books.csv", index=False)

        time.sleep(5)

    else:
        print(f"[INFO] Book: {title} - {author}, has cover. Skipping.")
