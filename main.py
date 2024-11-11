import sys
import logging
from PySide6.QtWidgets import QApplication

from user_interface.gui import MainWindow
from data_acquisition import api_fetcher, local_files
from data_processing.data_processor import DataProcessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        app = QApplication(sys.argv)

        logging.info("Initializing data fetchers and processor...")
        api_fetcher_instance = api_fetcher.ApiFetcher()
        # We don't need to instantiate local_files as it contains standalone functions
        data_proc = DataProcessor()

        logging.info("Creating main window...")
        main_window = MainWindow(api_fetcher_instance, local_files, data_proc)
        main_window.show()

        logging.info("Application started successfully.")
        sys.exit(app.exec_())
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
