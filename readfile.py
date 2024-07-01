def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("File content before writing:")
            print(content)
    except FileNotFoundError:
        print(f"{file_path} not found. There is nothing to read.")

# Example usage for reading the file
read_file("example1.txt")
