def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError as e:
        print(f"Error: {e}. The file was not found.")
    except IOError as e:
        print(f"Error: {e}. An I/O error occurred.")
    else:
        print("File read successfully.")
    finally:
        try:
            file.close()
        except NameError:
            print("File was never opened, no need to close.")
        except UnboundLocalError:
            print("File variable is not defined, skipping close operation.")
        print("Execution of the read_file function is complete.")

# Test cases
read_file("existing_file.txt")  # Assuming this file exists
read_file("non_existing_file.txt")  # This file does not exist
