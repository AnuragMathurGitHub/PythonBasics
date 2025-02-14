# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # apple
print(fruits[-1])  # cherry

# Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

# Adding and removing
fruits.append("mango")
fruits.remove("banana")

#fruits.pop()  # remove last item

fruits.sort()  # sort list
print(fruits)

fruits.reverse()  # reverse list
print(fruits)

# Key List Methods:
# .append(item) - Add item to end
# .remove(item) - Remove item
# .pop() - Remove and return last item
# .sort() - Sort list
# .reverse() - Reverse list
