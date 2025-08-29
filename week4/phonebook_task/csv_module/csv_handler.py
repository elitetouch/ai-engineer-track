# CSV Handler Module
import csv
from pathlib import Path

def create_workspace():
    workspace = Path("week4/phonebook_task/phonebook_data_files")
    workspace.mkdir(exist_ok=True)
    return workspace  


def store_data(file_path, data):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)  # Write all rows at once

    return True


def read_csv(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        return list(reader)
         # Alternative: Iterate over rows
        # for row_number, row in enumerate(reader):
        #     if row_number == 0:  # Header row
        #         print(f"Headers: {' | '.join(row)}")
        #         print("-" * 40)
        #     else:  # Data rows
        #         fullname, phone, age, track = row
        #         print(f"{fullname} ({phone} years) - {track}: {age}")


def remove_data(file_path, row_to_remove):
    data = read_csv(file_path)
    if not data:
        return False

    # Remove the specified row
    if 0 <= row_to_remove < len(data):
        del data[row_to_remove]
        store_data(file_path, data)
        return True
    return False


def update_data(file_path, row_to_update, new_data):
    data = read_csv(file_path)
    if not data:
        return False

    # Update the specified row
    if 0 <= row_to_update < len(data):
        data[row_to_update] = new_data
        store_data(file_path, data)
        return True
    return False    
