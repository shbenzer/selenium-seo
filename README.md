# SeleniumSEO
SeleniumSEO is a Python package designed to help with SEO keyword extraction from web pages using Selenium and BeautifulSoup. It allows you to extract and analyze content from specified HTML tags (like paragraphs, headings, and lists), clean the data by removing stop words, and generate a keyword frequency report. This is particularly useful for SEO professionals and web scraping enthusiasts looking to analyze web pages for SEO optimization.

## Features
Extracts text from common HTML tags like `<p>, <h1>, <h2>, <h3>, and <li>.`
- Cleans the extracted text by removing common stop words.
- Removes non-alphabetical characters to focus on meaningful keywords.
- Provides a frequency count of keywords from a webpage.
- Easily configurable to specify custom tags and stop words.

## Installation
You can install selenium-seo via pip. First, make sure you have Selenium and BeautifulSoup installed, as they are required dependencies:
```bash
pip install selenium beautifulsoup4
```
Then, install selenium-seo:
```bash
pip install selenium-seo
```

## Usage
Here's a basic example of how to use the SeleniumSEO class to extract and analyze keywords from a webpage:

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium_seo import SeleniumSEO

# Initialize WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Specify the URL to scrape
url = "https://www.example.com"
driver.get(url)

# Wait for the page to fully load
WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

# Initialize the SeleniumSEO class with the driver
seo = SeleniumSEO(driver)

# Get the cleaned keyword frequencies
keywords = seo.process_keywords()

# Print the keywords and their counts
for word, count in keywords:
    print(f"{word}: {count}")

# Close the driver after scraping
driver.quit()
```

## Available Methods

```process_keywords()```
Extracts keywords from the page and returns a sorted list of keywords with their frequency count.

```set_tags(tags)```
Sets the tags to be processed (default: ['p', 'h1', 'h2', 'h3', 'li']).

```get_tags()```
Returns the current tags being processed.

```set_ignore_words(words)```
Sets the list of stop words to ignore during keyword extraction.

```get_ignore_words()```
Returns the current list of stop words being ignored.

## License
This project is licensed under the terms of the Apache License 2.0.

## Acknowledgments
Selenium for browser automation.
BeautifulSoup for HTML parsing.
