from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit
from PySide6.QtCore import Qt
from data_acquisition.social_media import fetch_x_data
from data_processing.text_processing import process_text
import traceback

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dataset Generator")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create buttons
        button_layout = QHBoxLayout()
        self.web_scraping_btn = QPushButton("Web Scraping")
        self.social_media_btn = QPushButton("Social Media")
        self.public_datasets_btn = QPushButton("Public Datasets")
        self.local_files_btn = QPushButton("Local Files")

        button_layout.addWidget(self.web_scraping_btn)
        button_layout.addWidget(self.social_media_btn)
        button_layout.addWidget(self.public_datasets_btn)
        button_layout.addWidget(self.local_files_btn)

        main_layout.addLayout(button_layout)

        # Create text area for displaying results
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        main_layout.addWidget(self.result_text)

        # Create status label
        self.status_label = QLabel("Ready")
        main_layout.addWidget(self.status_label)

        # Connect buttons to functions
        self.web_scraping_btn.clicked.connect(self.web_scraping)
        self.social_media_btn.clicked.connect(self.social_media)
        self.public_datasets_btn.clicked.connect(self.public_datasets)
        self.local_files_btn.clicked.connect(self.local_files)

    def web_scraping(self):
        self.status_label.setText("Web scraping in progress...")
        # Implement web scraping logic here

    def social_media(self):
        self.status_label.setText("Collecting social media data...")
        try:
            # Example: Fetch data from X
            x_data = fetch_x_data("python", 10)
            if x_data:
                processed_data = [process_text(post['text']) for post in x_data]
                self.result_text.setText("\n".join(processed_data))
            else:
                self.result_text.setText("No data fetched from X. Check your X_BEARER_TOKEN and network connection.")
        except Exception as e:
            error_msg = f"Error fetching data: {str(e)}\n\n"
            error_msg += traceback.format_exc()
            self.result_text.setText(error_msg)
        finally:
            self.status_label.setText("Ready")

    def public_datasets(self):
        self.status_label.setText("Accessing public datasets...")
        # Implement public dataset access logic here

    def local_files(self):
        self.status_label.setText("Importing local files...")
        # Implement local file import logic here
