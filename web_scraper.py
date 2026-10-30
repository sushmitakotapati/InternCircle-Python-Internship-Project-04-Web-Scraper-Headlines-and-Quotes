
import requests
from bs4 import BeautifulSoup
import json
import time
from pathlib import Path

url = "https://quotes.toscrape.com/"
output_file = Path(__file__).parent / "quotes.json"

QUOTE_SELECTOR = "div.quote"
TEXT_SELECTOR = "span.text"
AUTHOR_SELECTOR = "small.author"

try:
    print("Connecting to website...")

    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "StudentPracticeScraper/1.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for item in soup.select(QUOTE_SELECTOR)[:20]:
        quote_element = item.select_one(TEXT_SELECTOR)
        author_element = item.select_one(AUTHOR_SELECTOR)

        if quote_element is None or author_element is None:
            continue

        quotes.append({
            "quote": quote_element.get_text(strip=True),
            "author": author_element.get_text(strip=True)
        })

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(quotes, file, indent=4, ensure_ascii=False)

    print("Quotes extracted successfully!")
    print("Total quotes:", len(quotes))
    print("Saved to:", output_file)

    time.sleep(1)

except requests.exceptions.RequestException as error:
    print("Website request failed:", error)

except (OSError, ValueError) as error:
    print("File or data error:", error)
