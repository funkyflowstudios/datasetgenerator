import pandas as pd
from typing import List, Dict, Any
import sys

class DataProcessor:
    def __init__(self):
        pass

    def process_data(self, data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
        """
        Process the input data and return a pandas DataFrame.
        """
        if not data:
            return pd.DataFrame()

        df = pd.DataFrame(data)
        if columns:
            df = df[columns]
        return df

    def export_to_csv(self, df: pd.DataFrame, filename: str) -> None:
        """
        Export the processed data to a CSV file.
        """
        try:
            df.to_csv(filename, index=False)
            print(f"Data exported successfully to {filename}")
        except Exception as e:
            print(f"Error exporting data to CSV: {e}")
            sys.exit(1)  # Exit the program with an error code

# Keep the original functions for backwards compatibility
def process_data(data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
    return DataProcessor().process_data(data, columns)

def export_to_csv(df: pd.DataFrame, filename: str) -> None:
    DataProcessor().export_to_csv(df, filename)