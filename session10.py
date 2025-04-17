# Date: 15/04/2025
# ==========================================================
# Decorators in Python

# intro:
    # 
# In python, fucntions are first class objects, meaning they can be passed around as arguments to other functions, returned from other functions, and assigned to variables.
# This allows for a powerful programming paradigm known as functional programming.
# Functions are first- class citizen in the memory and can be used as arguments to other functions as follows:
def calculate_math (a, b, operation):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    else:
        return "Invalid operation"
    
print(calculate_math) # Output: <function calculate_math at 0x7f8e4c1d3e50>
result = calculate_math(10, 5, "add")
print(result)  # Output: 15

# what is a decorator?
    # A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.


# ===========================================
# Generators in Python

#TODO: 