import pandas as pd
import os

def load_local_file(file_path):
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}"

    try:
        _, file_extension = os.path.splitext(file_path)
        if file_extension.lower() == '.csv':
            data = pd.read_csv(file_path)
        elif file_extension.lower() in ['.xls', '.xlsx']:
            data = pd.read_excel(file_path)
        else:
            return f"Error: Unsupported file format {file_extension}"

        return data
    except Exception as e:
        return f"Error loading file: {str(e)}"

# Remove or comment out the example usage at the bottom of the file
# file_path = 'data/example.csv'
# data = load_local_file(file_path)
# print(data)
