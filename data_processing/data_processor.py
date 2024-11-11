import pandas as pd
from typing import List, Dict, Any
from textblob import TextBlob

class DataProcessor:
    def process_data(self, data):
        if isinstance(data, pd.DataFrame):
            df = data
        else:
            df = pd.DataFrame(data)

        if df.empty:
            return df  # Return empty DataFrame if input is empty

        # Check if 'text' column exists, if not, try to use 'title' or the first string column
        text_columns = ['text', 'title'] + df.select_dtypes(include=['object']).columns.tolist()
        text_column = next((col for col in text_columns if col in df.columns), None)

        if text_column is None:
            raise ValueError("No suitable text column found for sentiment analysis")

        # Apply sentiment analysis
        df['sentiment'] = df[text_column].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        return df

def process_data(data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
    # This function is kept for backward compatibility
    processor = DataProcessor()
    return processor.process_data(data)

class DataProcessor:
    def process_data(self, data):
        if isinstance(data, pd.DataFrame):
            df = data
        else:
            df = pd.DataFrame(data)

        if df.empty:
            return df  # Return empty DataFrame if input is empty
        # Check if 'text' column exists, if not, try to use 'title' or the first string column
        text_columns = ['text', 'title'] + df.select_dtypes(include=['object']).columns.tolist()
        text_column = next((col for col in text_columns if col in df.columns), None)

        if text_column is None:
            raise ValueError("No suitable text column found for sentiment analysis")
        # Apply sentiment analysis
        df['sentiment'] = df[text_column].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        return df
# Keep the original functions for backwards compatibility
def process_data(data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
    return DataProcessor().process_data(data, columns)

def export_to_csv(df: pd.DataFrame, filename: str) -> None:
    DataProcessor().export_to_csv(df, filename)