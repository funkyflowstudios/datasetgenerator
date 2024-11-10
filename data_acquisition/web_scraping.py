import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data from the soup object
        # This is just an example, adjust according to your needs
        title = soup.title.string if soup.title else "No title found"
        paragraphs = [p.text for p in soup.find_all('p')]

        return {
            'title': title,
            'paragraphs': paragraphs
        }
    except requests.RequestException as e:
        return f"Error scraping website: {str(e)}"

# Remove or comment out the example usage
# url = 'https://www.example.com'
# data = scrape_website(url)
# print(data)
