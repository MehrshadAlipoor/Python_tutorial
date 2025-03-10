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

# finding max number

outnumbers = list(range(1, 100))

max = outnumbers[0]

for number in outnumbers:
    if number > max:
        max = number

print(max)

# list methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
    # example: numbers.pop(0)  # removes the first element
# remove()	Removes the item with the specified value
# in the list
    #example: print(50 in numbers)  # True
# sort()	Sorts  the list
    # example: numbers.sort() # [1, 2, 3, 4, 5]


# ================================================================================================

# Tuple
coordinates = (1, 2, 3)
# we can't change the value of a tuple
# coordinates[1] = 10  # TypeError: 'tuple' object does not support item assignment

# tuple methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Set
colors = {"red", "green", "blue"}

# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# dictionary items
    # keys()	Returns a list containing the dictionary's keys
    # values()	Returns a list containing the dictionary's values

# dictionary methods

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key to avoid KeyError
    # example: print(person.get("name"))  # John
# items()	Returns a list containing a tuple for each key value pair
    # example: print(person.items())  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
# keys()	Returns a list containing the dictionary's keys
    #example: print(person.keys())  # dict_keys(['name', 'age', 'city'])
# pop()	Removes the element with the specified key

# exercise: emoji converter
'''
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😢"
}
output = ""
for word in words: # O(n)
    output += emojis.get(word, word) + " "
print(output)
'''
# ================================================================================================
# A quick tip about functions

# in function to pass an argument to a function use keyword argument after positional argument
# example: def greet_user(first_name, last_name):  # positional argument
# greet_user(first_name="John", last_name="Doe")  # keyword argument


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

# Unpacking

numbers = [1, 2, 3]
x, y, z = numbers
print(x)  # 1
print(y)  # 2
print(z)  # 3

# ================================================================================================
# exceptions
# we use try and except block to handle exceptions
# it helps to handle errors and avoid program crash
# example: ValueError, ZeroDivisionError, FileNotFoundError, etc

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

# use comments to explain whys and hows not whats

# ================================================================================================