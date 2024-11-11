import nltk
import os

def download_nltk_data():
    """
    Download required NLTK data if not already present.
    """
    required_packages = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger', 'punkt_tab']

    for package in required_packages:
        try:
            if package == 'punkt_tab':
                nltk.data.find(f'tokenizers/{package}/english/')
            else:
                nltk.data.find(f'tokenizers/{package}')
            print(f"{package} is already downloaded.")
        except LookupError:
            print(f"Downloading {package}...")
            nltk.download(package, quiet=True)
            print(f"{package} has been downloaded successfully.")

if __name__ == "__main__":
    print("Checking and downloading required NLTK data...")
    download_nltk_data()
    print("NLTK data check and download completed.")