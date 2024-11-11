import requests
from typing import Dict, Any

def fetch_data_from_api(url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Fetch data from a RESTful API.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return {}