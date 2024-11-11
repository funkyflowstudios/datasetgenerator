import os
import csv
import io

def read_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        content = csvfile.read().strip()

        if not content:
            return []

        # Use StringIO to create a file-like object from the string
        csv_io = io.StringIO(content)
        reader = csv.reader(csv_io)

        try:
            header = next(reader)
            if not header:
                return []

            rows = []
            for row in reader:
                if len(row) != len(header):
                    raise csv.Error("Mismatched number of columns")
                rows.append(dict(zip(header, row)))

            return rows
        except csv.Error as e:
            raise csv.Error(f"Invalid CSV: {str(e)}")

def list_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory does not exist: {directory_path}")
    return os.listdir(directory_path)

# You can keep any existing functions here

# Example usage
if __name__ == "__main__":
    file_path = 'path/to/your/local/file.csv'  # Replace with an actual file path
    data = load_local_file(file_path)
    if data is not None:
        print(f"Loaded data with shape: {data.shape}")
        print(data.head())

