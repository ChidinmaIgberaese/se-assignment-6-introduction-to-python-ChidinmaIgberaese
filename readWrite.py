# Function to read from a file
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("File content before writing:")
            print(content)
            return content  # Return the content read from the file
    except FileNotFoundError:
        print(f"{file_path} not found. There is nothing to read.")
        return None  # Return None if the file does not exist

# Example usage for reading the file
read_content = read_file("example1.txt")

# Function to write to a file
def write_file(file_path, content_to_write):
    with open(file_path, "w") as file:
        file.write(content_to_write)
        print(f"New content written to {file_path}")

# Example usage for writing to the file
content_to_write = "How brilliant that I can write to a file!"
write_file("example2.txt", content_to_write)

# Verify the write operation by reading the file again
if read_content is not None:
    read_file("example2.txt")
