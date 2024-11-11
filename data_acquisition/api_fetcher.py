import requests

class ApiFetcher:
    def __init__(self):
        self.base_url = "https://api.example.com"  # Replace with your actual API base URL

    def fetch_data(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()

    # Add more methods as needed for different API endpoints or data sources