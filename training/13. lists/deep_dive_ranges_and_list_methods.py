# Understanding memory efficiency with range

# Let's define a range from 0 to 999,999
large_range = range(1000000)

# This does not take up a lot of memory because it doesn't generate all numbers at once
print("Size of large range:", large_range)  # Outputs: range(0, 1000000)

# Check if a number is in range without generating all numbers
print("Is 500,000 in the range?", 500000 in large_range)  # Outputs: True

# Trying to modify a range will lead to an error (demonstrates immutability)
try:
    large_range[0] = 10
except TypeError as e:
    print("Error:", e)  # Outputs: 'range' object does not support item assignment

# Checking membership efficiently
print("Is 100 included in range(0, 200, 2)?", 100 in range(0, 200, 2))  # Outputs: True
print("Is 101 included in range(0, 200, 2)?", 101 in range(0, 200, 2))  # Outputs: False

# PLEASE NOTE: range is a very efficient way to handle sequences of numbers!
# THANK YOU for exploring the memory and performance advantages of range objects with me!


# Creating a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# 1. append(): Adds 'elderberry' to the end of the list
fruits.append("elderberry")
print("After append:", fruits)  # Outputs: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 2. extend(): Adds elements of another list to the end
fruits.extend(["fig", "grape"])
print("After extend:", fruits)  # Outputs: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# 3. insert(): Inserts 'apricot' at index 1
fruits.insert(1, "apricot")
print("After insert:", fruits)  # Outputs: ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# 4. remove(): Removes the first occurrence of 'banana'
fruits.remove("banana")
print("After remove:", fruits)  # Outputs: ['apple', 'apricot', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# 5. pop(): Removes and returns the last element ('grape')
popped = fruits.pop()
print("Popped element:", popped)  # Outputs: 'grape'
print("After pop:", fruits)  # Outputs: ['apple', 'apricot', 'cherry', 'date', 'elderberry', 'fig']

# 6. clear(): Empties the list
fruits.clear()
print("After clear:", fruits)  # Outputs: []

# Resetting the list for further examples
fruits = ["apple", "apricot", "banana", "cherry", "date", "elderberry", "fig"]

# 7. index(): Finds the index of 'cherry'
index = fruits.index("cherry")
print("Index of 'cherry':", index)  # Outputs: 3

# 8. count(): Counts the occurrences of 'apple'
count = fruits.count("apple")
print("Count of 'apple':", count)  # Outputs: 1

# 9. sort(): Sorts the list in ascending order
fruits.sort()
print("After sort (ascending):", fruits)  # Outputs: ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry', 'fig']

print (f"lista original{fruits}")

posición = id(fruits)

print (f"lista posición es {id}")