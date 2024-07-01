def write_file(file_path, content_to_write):
    with open(file_path, "w") as file:
        file.write(content_to_write)
        print(f"New content written to {file_path}")

# Example usage for writing to the file
content_to_write = "How brilliant that I can write to a file!"
write_file("example2.txt", content_to_write)


