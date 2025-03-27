# parameter vs argument
# parameter is a variable in a method definition
# argument is the actual value of this variable that gets passed to the method
# In other words, when you define a function, you write parameters. When you call a function, you provide arguments.
# In the function definition, the parameter is the variable name that appears in the function definition.
# In the function call, the argument is the value that is sent to the function when it is called.
# In other words, a parameter is the variable in the declaration of a function.

# 1. Write a function that takes a string as an argument and returns the string reversed.

def reverse_string(string):
    return string[::-1]


# 2. Write a function that takes a string as an argument and returns the string reversed.
#    Use a for loop to reverse the string.

def reverse_string_for_loop(string):
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


# 3. Write a function that takes a string as an argument and returns the string reversed.
#    Use a while loop to reverse the string.

def reverse_string_while_loop(string):
    reversed_string = ''
    i = len(string) - 1
    while i >= 0:
        reversed_string += string[i]
        i -= 1
    return reversed_string

# 4. Write a function that takes a string as an argument and returns the string reversed.
#    Use recursion to reverse the string.

def reverse_string_recursion(string):
    '''This function reverses a string using recursion'''
    if len(string) == 0:
        return string
    else:
        return reverse_string_recursion(string[1:]) + string[0]
    
# 5. Write a function that takes a list of numbers as an argument and returns the sum of the numbers.

def sum_of_numbers(numbers):
    return sum(numbers)

# calling the functions
print(reverse_string('hello'))
print(reverse_string_for_loop('hello'))
print(reverse_string_while_loop('hello'))
print(reverse_string_recursion('hello'))
print(sum_of_numbers([1, 2, 3, 4, 5]))

    
#==================================================================================================
# dynamic type in python is a feature that allows you to change the type of a variable during runtime
# In Python, a variable is a name that you associate with a particular object.
# The variable can be reassigned to refer to a different object of the same type, or a different type.
# The type of a variable is determined by the type of the object it refers to.
# example:
    # x = 5
    # x = 'hello'
    # x = [1, 2, 3]
    # x = {'name': 'John', 'age': 25}
# In the above example, the variable x is first assigned an integer value, then a string value, then a list value, and finally a dictionary value.
# This is possible because Python is a dynamically typed language, which means that you can change the type of a variable during runtime.


# ==================================================================================================
#print function parameters
    # sep: separator between the arguments to print (default: ' ')
    # end: end of line character (default: '\n')
        # example:
        # print('hello', 'world', sep=', ', end='!')
        # output: hello, world!
    
        
print('hello', 'world', sep=', ', end='!')

# ==================================================================================================
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# True and True = True
# True and False = False
# False and True = False
# False and False = False

# not True = False
# not False = True

# ==================================================================================================