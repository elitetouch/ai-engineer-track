import csv_handler as csvm

def main():
    workspace = csvm.create_workspace()
    print(f"Workspace created at: {workspace}")

    # Sample data
    data = [
        ["fullname", "phone", "age", "track"],
        ["John Doe", "123-456-7890", "30", "AI"],
        ["Jane Smith", "987-654-3210", "25", "Web Development"],
    ]

    # Store data
    file_path = workspace / "phonebook.csv"
    csvm.store_data(file_path, data)

    # Read data
    read_data = csvm.read_csv(file_path)
    print("Data read from CSV:")
    for row in read_data:
        print(row)

    # Update data
    new_data = ["John Doe", "111-222-3333", "31", "AI"]
    csvm.update_data(file_path, 1, new_data)

    # Remove data
    csvm.remove_data(file_path, 0)

if __name__ == "__main__":
    main()
