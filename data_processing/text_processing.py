import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
def process_text(text):
    """
    Process the input text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): The input text to process.

    Returns:
        list: A list of processed words.
    """
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove punctuation and numbers
    tokens = [token for token in tokens if token not in string.punctuation and not token.isdigit()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return tokens
