import pandas as pd
import os

def load_local_file(file_path):
    """
    Load a local file into a pandas DataFrame.

    Args:
        file_path (str): Path to the local file.

    Returns:
        pandas.DataFrame: DataFrame containing the data from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format is unsupported.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    file_extension = os.path.splitext(file_path)[1].lower()
    try:
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        elif file_extension == '.json':
            df = pd.read_json(file_path)
        elif file_extension == '.txt':
            df = pd.read_csv(file_path, sep='\t')  # Assuming tab-separated
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        return df
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    file_path = 'path/to/your/local/file.csv'  # Replace with an actual file path
    data = load_local_file(file_path)
    if data is not None:
        print(f"Loaded data with shape: {data.shape}")
        print(data.head())
