from file_storage import FileStorage

def process_storage_operations(storage, key, value):
    storage.write(key, value)
    print(f"Data written: {key}")

    data = storage.read(key)
    print(f"Loaded {key}: {data}")

    if storage.exists(key):
        print(f"'{key}' exists.")
    else:
        print(f"'{key}' does not exist.")

    if storage.delete(key):
        print(f"'{key}' successfully deleted.")
    else:
        print(f"Failed to delete '{key}'.")

def main():
    # You can replace FileStorage with other storage implementations.
    storage = FileStorage(base_directory="data_storage")

    operations = [
        ("username.txt", "JohnDoe"),
        ("email.txt", "john.doe@example.com")
    ]

    for key, value in operations:
        process_storage_operations(storage, key, value)

if __name__ == "__main__":
    main()
