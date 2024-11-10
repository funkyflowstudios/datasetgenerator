import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from user_interface.gui import MainWindow
from data_acquisition.social_media import get_x_data, get_reddit_data
from data_acquisition.public_datasets import load_public_dataset
from data_acquisition.local_files import load_local_file
from scripts.download_nltk_data import download_nltk_data
import os

class AppDelegate(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def applicationSupportsSecureRestorableState(self):
        return True

def check_api_keys():
    api_keys = {
        'X_BEARER_TOKEN': os.getenv('X_BEARER_TOKEN'),
        'REDDIT_CLIENT_ID': os.getenv('REDDIT_CLIENT_ID'),
        'REDDIT_CLIENT_SECRET': os.getenv('REDDIT_CLIENT_SECRET'),
        'REDDIT_USER_AGENT': os.getenv('REDDIT_USER_AGENT')
    }

    print("Checking API keys:")
    for key, value in api_keys.items():
        if value:
            print(f"  {key}: {'*' * 8}{value[-4:] if value else ''}")
        else:
            print(f"  {key}: Not set")

def run():
    # Check API keys
    check_api_keys()

    # Ensure NLTK data is downloaded
    download_nltk_data()

    # Initialize and show the GUI
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
