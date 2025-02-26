# comparison operators
# ==, !=, >, <, >=, <=
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10 == "10")
print(10 != 10)
print("bag" > "apple" and "bag" > "cat")
print("bag" == "BAG")
print(ord("b"))  # ord() returns the ASCII value of a character
print(ord("B"))

# ================================================================================================
# conditional statements
# if, elif, else
# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of codeq

temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("\nDrink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's not a hot day")

# ================================================================================================
# ternary operator
# condition_if_true if condition else condition_if_false
age = 2
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
# ================================================================================================
# Logical operators
# and, or, not
high_income = True
good_credit = True
student = False

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# not operator
if not student:
    print("Eligible")
else:
    print("Not eligible")

# short circuitings in logical operators

# ================================================================================================
# chaining comparison operators
# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")

# ================================================================================================
# for loops
# for item in "Python": # item is a variable that will hold each character in the string
#     print(item)
# for item in ["a", "b", "c"]:  # item is a variable that will hold each item in the list
#     print(item)

for number in range(3):  # range(3) returns a sequence of numbers from 0 to 2
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range(1, 4) returns a sequence of numbers from 1 to 3
    print("Attempt", number, number * ".")

# range(1, 10, 2) returns a sequence of numbers from 1 to 9 with a step of 2
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# nested loops
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# ================================================================================================
# Iterables
# list, tuple, set, string, range, dictionary
# for item in "Python":
#     print(item)   # item is a variable that will hold each character in the string
# for item in ["a", "b", "c"]:
#     print(item)   # item is a variable that will hold each item in the list
# for item in (1, 2, 3):
#     print(item)   # item is a variable that will hold each item in the tuple
# for item in {1, 2, 3}:  # set
#     print(item)   # item is a variable that will hold each item in the set
# for item in {"name": "John", "age": 30}:
#     print(item)   # item is a variable that will hold each key in the dictionary
# for item in range(5):
#     print(item)   # item is a variable that will hold each
# ================================================================================================
# While loops
# while condition:
#     block of code
number = 100
while number > 0:
    print(number)
    number //= 2  # integer division

'''command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
'''
# ================================================================================================
# Infinite loops
# while True:
#     command = input(">")
#     print("ECHO", command)
# ================================================================================================

# functions


def greet_user():
    print("Hi there!")
    print("Welcome aboard")


greet_user()
# parameters vs arguments
# parameters are the names of the variables that you define in the function signature
# arguments are the values that you pass to the function when you call it


def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")


greet_user("John")
greet_user("Mary")

# types of functions

# 1. Perform a task


def greet_user():
    print("Hi there!")
    print("Welcome aboard")


greet_user()

# 2. Return a value


def greet_user():
    return "Hi there!"


message = greet_user()
print(message)

# 3. Perform a task and return a value


def greet_user(name):
    return f"Hi {name}!"


message = greet_user("John")
print(message)

# 4. Accept multiple arguments


def greet_user(first_name, last_name):
    return f"Hi {first_name} {last_name}!"


message = greet_user("John", "Smith")
print(message)
