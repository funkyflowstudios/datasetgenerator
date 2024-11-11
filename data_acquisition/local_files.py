import pandas as pd
import json

def read_file(file_path):
    try:
        if file_path.endswith('.csv'):
            # Try reading CSV with different encodings
            encodings = ['utf-8', 'iso-8859-1', 'cp1252']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                raise ValueError("Unable to decode the CSV file with known encodings.")
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as f:
                data = json.load(f)
            df = pd.DataFrame(data)
        else:
            raise ValueError("Unsupported file type. Please use CSV or JSON.")

        if df.empty:
            print("Warning: The file is empty")

        return df
    except pd.errors.EmptyDataError:
        print("The file is empty or contains no valid data.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return pd.DataFrame()

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