import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, elements_to_scrape):
    """
    Scrape data from a given URL.
    
    :param url: The URL of the website to scrape
    :param elements_to_scrape: A list of dictionaries, each containing 'name' and 'selector'
    :return: A pandas DataFrame with the scraped data
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data = {elem['name']: [] for elem in elements_to_scrape}
        
        # Find the maximum number of items
        max_items = max(len(soup.select(elem['selector'])) for elem in elements_to_scrape)
        
        for i in range(max_items):
            for elem in elements_to_scrape:
                items = soup.select(elem['selector'])
                if i < len(items):
                    data[elem['name']].append(items[i].get_text(strip=True))
                else:
                    data[elem['name']].append(None)
        
        return pd.DataFrame(data)
    
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return pd.DataFrame()

# Example usage:
# elements = [
#     {'name': 'title', 'selector': 'h1'},
#     {'name': 'paragraph', 'selector': 'p'},
# ]
# df = scrape_website('https://example.com', elements)