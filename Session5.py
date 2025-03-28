# Date: 2025/03/27

#==================================================================================================
# anonymous functions (lambda functions) in Python:


# Map function in Python:
    # The map() function in Python takes in a function and a list as arguments
    # and returns a new list with the function applied to each element in the original list.
    # The map() function can be used to apply a function to multiple elements in a list simultaneously.
    # The map() function is a higher-order function, which means it takes another function as an argument.
    # The map() function is a built-in function in Python, so you don't need to import any module to use it.
    # The map() function creates an object that can be converted to a list when needed.
        # example: 
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = print(list(map(square, numbers)))
    # The map() function can be used with lambda functions to apply a function to multiple elements in a list.
        # example: 

multiplied_numbers = map(lambda x: x * 2, numbers)
print(list(multiplied_numbers))

# Filter function in Python:
    # The filter() function in Python takes in a function and a list as arguments
    # and returns a new list with the elements for which the function returns True.
    # The filter() function can be used to filter elements from a list based on a condition.
    # The filter() function is a higher-order function, which means it takes another function as an argument.
    # The filter() function is a built-in function in Python, so you don't need to import any module to use it.
    # The filter() function creates an object that can be converted to a list when needed.
        # example:

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# old method:
even_numbers = []
for number in numbers:
    if is_even(number):
        even_numbers.append(number)

print(even_numbers)

# with anonymous function:

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# Lazy calling of functions in Python:

# ==================================================================================================
# scope v
    # legb rule:
        # L: Local
        # E: Enclosing
        # G: Global
        # B: Built-in
    # Local scope:
        # - The local scope: is the innermost scope: in Python. 
        # - It means that it is the scope that contains the local variables.
        # - Variables defined inside a function are in the local scope.
        # - Local variables are only accessible within the function in which they are defined.
    # example:
def my_function():
    x = 10
    print(x)
my_function()
        # - In this example, the variable x is defined inside the my_function() and accessed within the function.
        # - The variable x is in the local scope of the my_function().
        
   # Enclosing scope:
        # - The enclosing scope is the scope that contains the local scope.
        # - Enclosing variables are accessible within the function in which they are defined and any nested functions.
        # - Enclosing variables are not accessible outside the function in which they are defined.
        # example:
def outer_function():
    x = 10
    def inner_function():
        print(x)
    inner_function()
outer_function()
        # - In this example, the variable x is defined in the outer_function() and accessed in the inner_function().
        # - The variable x is in the enclosing scope of the inner_function().
        # - Enclosing variables are accessible within the function in which they are defined and any nested functions.
        # - Enclosing variables are not accessible outside the function in which they are defined.


    # Global scope:
        # - The global scope is the outermost scope in Python.
        # - Variables defined outside any function are in the global scope.
        # - Global variables are accessible from anywhere in the program.
            # example of global scope:
x = 10
def my_function():
    print(x)
my_function()
        # - Global variables can be accessed and modified from within a function.
        # - If a variable is modified inside a function, it will create a new local variable with the same name.
        # - To modify a global variable inside a function, you need to use the global keyword.
            # example:

x = 10
def my_function():
    global x
    x = 20
    print(x)
my_function()
        # - The global keyword is used to declare a variable as global inside a function.
        # - When you use the global keyword, you are telling Python that the variable is defined in the global scope.
        # - The global keyword is used to modify a global variable inside a function.
        # - If you don't use the global keyword, Python will create a new local variable with the same name.



    # Built-in scope:
        # - The built-in scope is the scope that contains the built-in functions and modules in Python.
        # - Built-in variables are accessible from anywhere in the program.
        # Example:
        
print(abs(-10))
# in this example, the abs() function is a built-in function in Python.
# The abs() function is in the built-in scope.

# ==================================================================================================