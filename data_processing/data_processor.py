import pandas as pd
from typing import List, Dict, Any
import sys
import re
import spacy
from textblob import TextBlob

class DataProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_data(self, data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
        """
        Process the input data and return a pandas DataFrame.
        """
        if not data:
            return pd.DataFrame()

        if columns is None:
            columns = [key for key in data[0].keys()]

        df = pd.DataFrame(data, columns=columns)
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

    def clean_text(self, text: str) -> str:
        """
        Clean the input text by removing special characters, extra whitespace, and converting to lowercase.
        """
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase and remove extra whitespace
        text = ' '.join(text.lower().split())
        return text

    def extract_entities(self, text: str) -> List[str]:
        """
        Extract named entities from the input text using spaCy.
        """
        doc = self.nlp(text)
        entities = [ent.text for ent in doc.ents]
        return entities

    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Perform sentiment analysis on the input text using TextBlob.
        """
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }
# Keep the original functions for backwards compatibility
def process_data(data: List[Dict[str, Any]], columns: List[str] = None) -> pd.DataFrame:
    return DataProcessor().process_data(data, columns)

def export_to_csv(df: pd.DataFrame, filename: str) -> None:
    DataProcessor().export_to_csv(df, filename)