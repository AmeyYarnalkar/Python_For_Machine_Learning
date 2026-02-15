# =====================================
# PYTHON DICTIONARY - BEGINNER EXAMPLES
# =====================================

# Creating dictionary
student = {
    "name": "Amey",
    "age": 21,
    "marks": 90
}

print("Original dict:", student)


# Access value using key
print("Name:", student["name"])


# Adding new element
student["city"] = "Pune"
print("After adding city:", student)


# Updating value
student["age"] = 22
print("After updating age:", student)


# Deleting element
del student["marks"]
print("After deleting marks:", student)


# Safe access using get()
print("Phone:", student.get("phone"))  # returns None if not present


# Getting keys
print("Keys:", student.keys())

# Getting values
print("Values:", student.values())

# Getting key-value pairs
print("Items:", student.items())


# Iterating keys
for key in student:
    print("Key:", key)

# Iterating values
for value in student.values():
    print("Value:", value)

# Iterating key-value pairs
for key, value in student.items():
    print(key, "->", value)


# Clearing dictionary
student.clear()
print("After clear:", student)
