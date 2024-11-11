import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys
import os
import string
import logging

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.download_nltk_data import download_nltk_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_text(text, join_tokens=False):
    """
    Process the input text by tokenizing, removing punctuation and stopwords, and lemmatizing.

    Args:
    text (str): The input text to process.
    join_tokens (bool): If True, join the processed tokens into a string. Default is False.

    Returns:
    list or str: A list of processed tokens, or a string if join_tokens is True.
    Returns None if an error occurs during processing.
    """
    try:
        # Ensure NLTK data is downloaded
        download_nltk_data()

        # Tokenization and lowercasing
        tokens = word_tokenize(text.lower())

        # Remove punctuation
        tokens = [token for token in tokens if token not in string.punctuation]

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        if join_tokens:
            return ' '.join(tokens)
        return tokens

    except Exception as e:
        logger.error(f"An error occurred while processing text: {str(e)}")
        return None

# You can add more text processing functions here if needed

# Example usage (commented out):
# processed_tokens = process_text("Your input text here.")
# processed_string = process_text("Your input text here.", join_tokens=True)
