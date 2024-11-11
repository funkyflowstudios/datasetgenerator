import sys
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit, QComboBox, QTextEdit, QFileDialog, QApplication
from PySide6.QtCore import Qt
import pandas as pd
from data_acquisition import social_media, local_files, web_scraper
from data_processing import DataProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dataset Generator")
        self.setGeometry(100, 100, 800, 600)

        self.fetched_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()
        self.data_processor = DataProcessor()

        self.url_input = None
        self.elements_input = None

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Input section
        input_layout = QHBoxLayout()
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter query")
        self.source_combo = QComboBox()
        self.source_combo.addItems(["X", "Reddit", "Local Files"])
        self.fetch_button = QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_data)

        input_layout.addWidget(self.query_input)
        input_layout.addWidget(self.source_combo)
        input_layout.addWidget(self.fetch_button)

        # Web scraping section
        scrape_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL to scrape")
        self.elements_input = QLineEdit()
        self.elements_input.setPlaceholderText("Enter elements to scrape (e.g., title:h1,paragraph:p)")
        self.scrape_button = QPushButton("Scrape Website")
        self.scrape_button.clicked.connect(self.scrape_website)

        scrape_layout.addWidget(self.url_input)
        scrape_layout.addWidget(self.elements_input)
        scrape_layout.addWidget(self.scrape_button)

        # Action buttons
        action_layout = QHBoxLayout()
        self.process_button = QPushButton("Process Data")
        self.process_button.clicked.connect(self.process_data)
        self.save_button = QPushButton("Save Dataset")
        self.save_button.clicked.connect(self.save_dataset)

        action_layout.addWidget(self.process_button)
        action_layout.addWidget(self.save_button)

        # Output section
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(scrape_layout)
        main_layout.addLayout(action_layout)
        main_layout.addWidget(self.output_text)

    def fetch_data(self):
        query = self.query_input.text()
        source = self.source_combo.currentText()
        if source == "X":
            self.fetched_data = pd.DataFrame(social_media.fetch_x_data(query, 10))
            self.output_text.append(f"Fetched {len(self.fetched_data)} X posts")
        elif source == "Reddit":
            self.fetched_data = pd.DataFrame(social_media.fetch_reddit_data(query, 10))
            self.output_text.append(f"Fetched {len(self.fetched_data)} Reddit posts")
        elif source == "Local Files":
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv);;JSON Files (*.json)")
            if file_path:
                self.fetched_data = local_files.read_file(file_path)
                if self.fetched_data.empty:
                    self.output_text.append(f"The file {file_path} is empty or contains no valid data.")
                else:
                    self.output_text.append(f"Loaded data from {file_path}")

        if not self.fetched_data.empty:
            self.output_text.append(f"Fetched {len(self.fetched_data)} items.")
            self.output_text.append(f"First item: {self.fetched_data.iloc[0].to_dict()}")
        else:
            self.output_text.append("No data fetched or the data is empty.")

    def scrape_website(self):
        url = self.url_input.text()
        elements_text = self.elements_input.text()
        
        if not url or not elements_text:
            self.output_text.append("Please enter both URL and elements to scrape.")
            return

        elements = [{'name': e.split(':')[0], 'selector': e.split(':')[1]} 
                    for e in elements_text.split(',')]

        self.output_text.append(f"Scraping {url}...")
        self.fetched_data = web_scraper.scrape_website(url, elements)

        if not self.fetched_data.empty:
            self.output_text.append(f"Scraped {len(self.fetched_data)} items.")
            self.output_text.append(f"First item: {self.fetched_data.iloc[0].to_dict()}")
        else:
            self.output_text.append("No data scraped or there was an error.")

    def process_data(self):
        if self.fetched_data.empty:
            self.output_text.append("No data to process. Please fetch data first.")
            return

        try:
            self.processed_data = self.data_processor.process_data(self.fetched_data)
            self.output_text.append(f"Processed {len(self.processed_data)} items.")
            self.output_text.append(f"First processed item: {self.processed_data.iloc[0].to_dict() if not self.processed_data.empty else 'No data'}")
        except Exception as e:
            self.output_text.append(f"Error processing data: {str(e)}")

    def save_dataset(self):
        if not self.processed_data.empty:
            data_to_save = self.processed_data
        elif not self.fetched_data.empty:
            data_to_save = self.fetched_data
        else:
            self.output_text.append("No data to save. Please fetch and process data first.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Dataset", "", "CSV Files (*.csv);;JSON Files (*.json)")
        if file_path:
            if file_path.endswith('.csv'):
                data_to_save.to_csv(file_path, index=False)
            elif file_path.endswith('.json'):
                data_to_save.to_json(file_path, orient='records')
            self.output_text.append(f"Dataset saved to {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())