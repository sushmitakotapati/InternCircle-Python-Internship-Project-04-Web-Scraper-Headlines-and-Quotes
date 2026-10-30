# Web Scraper for Headlines & Quotes

## Description
A simple Python web scraper that extracts quotes and author names from a public practice website using Requests and BeautifulSoup.

## Features
- Sends HTTP requests using the Requests library.
- Parses webpage HTML using BeautifulSoup.
- Extracts quotes and author names.
- Handles request errors and missing HTML elements.
- Saves extracted data in JSON format.
- Collects up to 20 records from the selected page.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON

## Data Source
[Quotes to Scrape](https://quotes.toscrape.com/)

This is a public practice website designed for learning web scraping. The project accesses its publicly available pages without logging in or collecting personal data.

## How to Run
1. Install the required libraries:
   `python -m pip install requests beautifulsoup4`
2. Run the program:
   `python web_scraper.py`
3. The extracted data is saved in `quotes.json`.

## Output
The program successfully extracted 10 quotes and saved them in JSON format.