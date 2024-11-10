import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

def scrape_website(url, max_pages=5):
    """
    Scrape a website, following links up to a maximum number of pages.

    Args:
        url (str): The starting URL to scrape.
        max_pages (int): Maximum number of pages to scrape. Defaults to 5.

    Returns:
        list: A list of dictionaries containing scraped data.
              Each dictionary has 'url', 'content', and 'title' keys.
    """
    scraped_data = []
    visited_urls = set()
    urls_to_visit = [url]

    headers = {
        'User-Agent': 'DatasetGenerator Bot 1.0',
    }

    for _ in range(max_pages):
        if not urls_to_visit:
            break

        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue

        visited_urls.add(current_url)

        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text content
            text_content = soup.get_text(separator=' ', strip=True)

            # Extract links
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('/'):
                    href = f"{urlparse(current_url).scheme}://{urlparse(current_url).netloc}{href}"
                if href.startswith('http') and href not in visited_urls:
                    urls_to_visit.append(href)

            scraped_data.append({
                'url': current_url,
                'content': text_content[:1000],  # Limit content to first 1000 characters
                'title': soup.title.string if soup.title else ''
            })

            time.sleep(1)  # Be polite, wait between requests

        except requests.RequestException as e:
            print(f"Error scraping {current_url}: {e}")

    return scraped_data

# Example usage
if __name__ == "__main__":
    url = 'https://www.example.com'
    data = scrape_website(url)
    print(f"Scraped {len(data)} pages")
    for item in data[:3]:  # Print first 3 items
        print(f"URL: {item['url']}")
        print(f"Title: {item['title']}")
        print(f"Content preview: {item['content'][:100]}...")
        print()
