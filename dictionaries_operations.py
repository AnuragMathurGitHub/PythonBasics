# Creating a dictionary
person = {
    "name": "Anurag",
    "age": 25,
    "city": "Munich"
}

# Accessing values
print(person["name"])
print(person.get("age"))

# Looping through keys & values
for key, value in person.items():
    print(key, ":", value)

# Adding a key-value pair
person["job"] = "Product Manager"
print(person)

print(person.items())
print(person.keys())
print(person.values())

# Key Dictionary Methods:
# .get(key) - Safely get value (avoids error)
# .keys() - Get all keys
# .values() - Get all values
# .items() - Get key-value pairs
