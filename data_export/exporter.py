import csv

def export_to_csv(data, file_path):
    if not data:
        raise ValueError("No data to export")

    keys = data[0].keys()

    with open(file_path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)