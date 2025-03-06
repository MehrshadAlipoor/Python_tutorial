# python
# Date: 06/03/2025

# ================================================================================================
prices = [10, 20, 30, 40, 50]
total = 0

for price in prices:
    total += price

print(f"Total: {total}")

# ================================================================================================
# Data Structures

# List: A list is a collection of items that are ordered and changeable. Lists are defined by square brackets [].
# Tuple: A tuple is a collection of items that are ordered and unchangeable. Tuples are defined by parentheses ().
# Set: A set is a collection of items that are unordered and unindexed. Sets are defined by curly braces {}.
# Dictionary: A dictionary is a collection of items that are unordered, changeable, and indexed. Dictionaries are defined by curly braces {}.


# List
numbers = [1, 2, 3, 4, 5]
names = ["John", "Jane", "Jack"]

print (names[0])  # John
print (names[-1])  # Jack
print (names[1:])  # ['Jane', 'Jack']   # slicing
print (names[1:3])  # ['Jane', 'Jack']  # slicing 

# Tuple
coordinates = (1, 2, 3)

# Set
colors = {"red", "green", "blue"}

# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# ================================================================================================

# reversed function
# The reversed() function returns a reverse iterator for a sequence.
# The reversed iterator can be converted to a list using the list() function.

numbers = [1, 2, 3, 4, 5]
strings = "Hello"

reversed_numbers = reversed(numbers)
reversed_strings = reversed(strings)
print(type(reversed_numbers))  # <class 'list_reverseiterator'>
type(reversed_strings)  # <class 'reversed'>

print(reversed_numbers)  # <list_reverseiterator object at 0x7f8b1b3b5d90>
print(list(reversed_numbers))  # [5, 4, 3, 2, 1]

print(reversed_strings)  # <reversed object at 0x7f8b1b3b5d90>
print(list(reversed_strings))  # ['o', 'l', 'l', 'e', 'H']

# ================================================================================================
# enumerate function
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# The enumerate object can be converted to a list using the list() function.

colors = ["red", "green", "blue"]

enumerate_colors = enumerate(colors)
print(type(enumerate_colors))  # <class 'enumerate'>

print(enumerate_colors)  # <enumerate object at 0x7f8b1b3b5d90>
print(list(enumerate_colors))  # [(0, 'red'), (1, 'green'), (2, 'blue')]

# ================================================================================================

# print an L

numbers = [2, 2, 2, 2, 8]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# print an M using a list of numbers
m_pattern = [
    'x     x',
    'xx   xx',
    'x x x x',
    'x  x  x',
    'x     x'
]

for line in m_pattern:
    print(line)
numbers = [8, 8, 8, 8, 8]
for x_count in range(len(numbers)):
    output = ''
    for count in range(numbers[x_count]):
        if x_count == 0:
            output = 'x     x'
        elif x_count == 1:
            output = 'xx   xx'
        elif x_count == 2:
            output = 'x x x x'
        elif x_count == 3:
            output = 'x  x  x'
        elif x_count == 4:
            output = 'x     x'
    print(output)

numbers = [2, 2, 2, 2, 8]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# ================================================================================================
