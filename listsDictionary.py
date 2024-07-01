# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Basic operations on the list
print("Original list:", numbers)

# Append an item to the list
numbers.append(6)
print("List after appending 6:", numbers)

# Remove an item from the list
numbers.remove(3)
print("List after removing 3:", numbers)

# Access an item by index
print("Item at index 2:", numbers[2])

# Creating a dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Basic operations on the dictionary
print("\nOriginal dictionary:", person)

# Add a key-value pair to the dictionary
person["email"] = "alice@example.com"
print("Dictionary after adding email:", person)

# Remove a key-value pair from the dictionary
del person["age"]
print("Dictionary after removing age:", person)

# Access a value by key
print("Value for key 'name':", person["name"])

# Check if a key exists in the dictionary
print("Is 'city' a key in the dictionary?", "city" in person)
