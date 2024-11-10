# public_datasets.py

import pandas as pd
import requests
from io import BytesIO
def load_public_dataset(dataset_name):
    """
    Load a public dataset from a predefined list or URL.

    Args:
        dataset_name (str): Name or URL of the dataset.

    Returns:
        pandas.DataFrame: DataFrame containing the dataset.

    Raises:
        ValueError: If the dataset name is unknown or the file format is unsupported.
    """
    # Predefined datasets
    datasets = {
        'iris': 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
        'wine': 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
        'boston_housing': 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
    }

    if dataset_name in datasets:
        url = datasets[dataset_name]
    elif dataset_name.startswith('http'):
        url = dataset_name
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    try:
        response = requests.get(url)
        response.raise_for_status()

        if url.endswith('.csv') or url.endswith('.data'):
            df = pd.read_csv(BytesIO(response.content), header=None)
        elif url.endswith('.xlsx'):
            df = pd.read_excel(BytesIO(response.content))
        else:
            raise ValueError(f"Unsupported file format for {url}")

        return df
    except requests.RequestException as e:
        print(f"Error fetching dataset: {e}")
        return None

# Example usage
if __name__ == "__main__":
    dataset = load_public_dataset('iris')
    if dataset is not None:
        print(f"Loaded dataset with shape: {dataset.shape}")
        print(dataset.head())
