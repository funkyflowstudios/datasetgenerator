import os
import csv
import io
import json
import pandas as pd

def read_file(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file type. Please use CSV or JSON.")

        return df.to_dict('records')
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return []

def list_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory does not exist: {directory_path}")
    return os.listdir(directory_path)

def save_to_csv(data, file_path):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Data saved to CSV: {file_path}")

def save_to_json(data, file_path):
    with open(file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    print(f"Data saved to JSON: {file_path}")

if __name__ == "__main__":
    print("This module provides functions for reading and writing local files.")