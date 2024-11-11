import sys
import logging
from PySide6.QtWidgets import QApplication

from user_interface.gui import MainWindow as GUI
from data_processing.data_processor import DataProcessor
from data_acquisition import local_files

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        app = QApplication(sys.argv)

        logging.info("Initializing data processor...")
        data_proc = DataProcessor()

        logging.info("Creating main window...")
        main_window = GUI(local_files, data_proc)
        main_window.show()

        logging.info("Application started successfully.")
        sys.exit(app.exec())
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
