import os


def handle_file_operations(directory, filename, content):
    filepath = os.path.join(directory, filename)

    with open(filepath, 'w') as file:
        file.write(content)

    with open(filepath, 'r') as file:
        data = file.read()

    print(f"Loaded {filename.split('.')[0]}: {data}")

    if os.path.exists(filepath):
        print(f"File '{filepath}' exists.")
    else:
        print(f"File '{filepath}' does not exist.")

    os.remove(filepath)
    print(f"Data deleted for {filename}.")

    if not os.path.exists(filepath):
        print(f"Key '{filename.split('.')[0]}' successfully deleted.")

def main():
    directory = "data_storage"
    
    handle_file_operations(directory, "username.txt", "JohnDoe")
    handle_file_operations(directory, "email.txt", "john.doe@example.com")

if __name__ == "__main__":
    main()

