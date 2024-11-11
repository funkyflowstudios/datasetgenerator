from PySide6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, QWidget, 
                               QPushButton, QLineEdit, QTextEdit, QHBoxLayout,
                               QFileDialog, QComboBox)
from data_acquisition import social_media, local_files
from data_processing import data_processor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data_processor = data_processor.DataProcessor()
        self.fetched_data = []
        self.processed_data = []

        self.setWindowTitle("Dataset Generator")
        self.setGeometry(100, 100, 800, 600)

        # Create main layout
        main_layout = QVBoxLayout()

        # Create input section
        input_layout = QHBoxLayout()
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter query or file path")
        self.source_combo = QComboBox()
        self.source_combo.addItems(["X", "Reddit", "Local Files"])
        fetch_button = QPushButton("Fetch Data")
        fetch_button.clicked.connect(self.fetch_data)
        input_layout.addWidget(self.query_input)
        input_layout.addWidget(self.source_combo)
        input_layout.addWidget(fetch_button)

        # Create output section
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Create process and save buttons
        process_button = QPushButton("Process Data")
        process_button.clicked.connect(self.process_data)
        save_button = QPushButton("Save Dataset")
        save_button.clicked.connect(self.save_dataset)

        # Add all components to main layout
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.output_text)
        main_layout.addWidget(process_button)
        main_layout.addWidget(save_button)

        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    def fetch_data(self):
        query = self.query_input.text()
        source = self.source_combo.currentText()

        if source == "X":
            self.fetched_data = social_media.fetch_x_data(query, 10)
            self.output_text.append(f"Fetched {len(self.fetched_data)} X posts")
        elif source == "Reddit":
            self.fetched_data = social_media.fetch_reddit_data(query, 10)
            self.output_text.append(f"Fetched {len(self.fetched_data)} Reddit posts")
        elif source == "Local Files":
            file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv);;JSON Files (*.json)")
            if file_path:
                self.fetched_data = local_files.read_file(file_path)
                self.output_text.append(f"Loaded data from {file_path}")

        self.output_text.append(f"First item: {self.fetched_data[0] if self.fetched_data else 'No data'}")

    def process_data(self):
        if not self.fetched_data:
            self.output_text.append("No data to process. Please fetch data first.")
            return

        try:
            self.processed_data = self.data_processor.process_data(self.fetched_data)
            self.output_text.append(f"Processed {len(self.processed_data)} items.")
            self.output_text.append(f"First processed item: {self.processed_data[0] if self.processed_data else 'No data'}")
        except Exception as e:
            self.output_text.append(f"Error processing data: {str(e)}")
    def save_dataset(self):
        data_to_save = self.processed_data if self.processed_data else self.fetched_data
        if not data_to_save:
            self.output_text.append("No data to save. Please fetch and process data first.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Dataset", "", "CSV Files (*.csv);;JSON Files (*.json)")
        if file_path:
            if file_path.endswith('.csv'):
                local_files.save_to_csv(data_to_save, file_path)
            elif file_path.endswith('.json'):
                local_files.save_to_json(data_to_save, file_path)
            self.output_text.append(f"Dataset saved to {file_path}")

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())