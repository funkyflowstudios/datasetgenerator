from PySide6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QWidget, 
                               QPushButton, QLineEdit, QTextEdit, QHBoxLayout)
from data_acquisition.social_media import fetch_x_data, fetch_reddit_data

class MainWindow(QMainWindow):
    def __init__(self, local_files, data_processor):
        super().__init__()

        self.local_files = local_files
        self.data_processor = data_processor

        self.setWindowTitle("Dataset Generator")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget and a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Add GUI components
        self.add_data_acquisition_section(main_layout)
        self.add_data_processing_section(main_layout)
        self.add_output_section(main_layout)

    def add_data_acquisition_section(self, layout):
        layout.addWidget(QLabel("Data Acquisition"))

        input_layout = QHBoxLayout()
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter search query")
        input_layout.addWidget(self.query_input)

        fetch_button = QPushButton("Fetch Data")
        fetch_button.clicked.connect(self.fetch_data)
        input_layout.addWidget(fetch_button)

        layout.addLayout(input_layout)

    def add_data_processing_section(self, layout):
        layout.addWidget(QLabel("Data Processing"))

        process_button = QPushButton("Process Data")
        process_button.clicked.connect(self.process_data)
        layout.addWidget(process_button)

    def add_output_section(self, layout):
        layout.addWidget(QLabel("Output"))

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

    def fetch_data(self):
        query = self.query_input.text()
        x_data = fetch_x_data(query, 10)
        reddit_data = fetch_reddit_data(query, 10)
        self.output_text.append(f"Fetched {len(x_data)} X posts and {len(reddit_data)} Reddit posts")

    def process_data(self):
        # This is a placeholder. Implement actual data processing logic here.
        self.output_text.append("Data processed successfully")
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow(None, None)  # Pass None for now as placeholders
    window.show()
    sys.exit(app.exec())