# Date: 25/03/2025
# ================== Session 4: Functions & Method (Cont.) ==================

# prosedural programming VS Functional programming:
    # 1. Procedural programming:
        # - Procedural programming is a programming paradigm that focuses on the process of creating a program.
        # - It is based on the concept of procedures or routines, which are sequences of instructions that perform a specific task.
        # - Procedural programming is a top-down approach to programming, where the program is divided into smaller procedures that are executed in a specific order.
        # - Examples of procedural programming languages include C, Pascal, and Fortran.

    # 2. Functional programming:
        # - Functional programming is a programming paradigm that focuses on the use of functions to perform computations.
        # - It is based on the concept of mathematical functions, which take input values and return output values without modifying the input values.
        # - Functional programming is a declarative approach to programming, where the program is expressed as a series of function calls that are composed together to form more complex functions.
        # - Examples of functional programming languages include Haskell, Lisp, and Clojure.


#==================================================================================================

# Guess a number game:

import random


def guess_number_game(guess):

    '''This function takes a number as a string argument 
    (expected to be convertible to an integer) and 
    compares it to a random number between 1 and 10.'''
    
    answer = random.randint(1, 10)
    try:
        guess = int(guess)
        if guess < 1 or guess > 10:
            print('Invalid input. Please enter a number between 1 and 10.')
            return False
        if guess > answer:
            print('Your guess is higher than the answer.')
        elif guess < answer:
            print('Your guess is lower than the answer.')
        elif guess == answer:
            print('Congratulations! You guessed the correct number.')
            return True
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
    return False

'''
while True:
    user_guess = input('Enter a num between 1 and 10:\n')
    if guess_number_game(user_guess):
        break
    '''
# ==================================================================================================

# args and kwargs in Python functions:
    # - args: a special syntax in Python that allows a function to accept a variable number of positional arguments.
    # - kwargs: a special syntax in Python that allows a function to accept a variable number of keyword arguments.
    # - kwargs: stands for keyword arguments
    # - args: stands for arguments
    # - args and kwargs are often used when you want to create a function that can accept a variable number of arguments, without having to specify the number of arguments in advance.
    # - when you use *args, it allows you to pass a variable number of positional arguments to the function.
    # - when you use **kwargs, it allows you to pass a variable number of keyword arguments to the function.
    # - by using *args it makes a tuple of the arguments passed to the function
    # - by using **kwargs it makes a dictionary of the arguments passed to the function

# positional arguments:
    # - Positional arguments are the arguments that are passed to a function in a specific order.
    # - The number of positional arguments that a function can accept is fixed and determined by the function definition.  

# keyword arguments:
    # - Keyword arguments are the arguments that are passed to a function with a keyword or parameter name.
    # - The number of keyword arguments that a function can accept is not fixed and can vary depending on the function definition.
    # - Keyword arguments are useful when you want to pass arguments to a function in a specific order, or when you want to specify default values for some arguments.

# difference between positional and keyword arguments:
    # - Positional arguments are passed to a function in a specific order, while keyword arguments are passed with a keyword or parameter name.
    # - The number of positional arguments that a function can accept is fixed and determined by the function definition, 
    # while the number of keyword arguments that a function can accept is not fixed and can vary depending on the function definition.
    # - Positional arguments are required, while keyword arguments are optional.
    # - Positional arguments are used when you want to pass arguments to a function in a specific order, 
    # while keyword arguments are used when you want to specify default values for some arguments.
    # - positional arguments follow keyword arguments in the function definition.
    # it means that you cannot have a positional argument after a keyword argument in the function definition.
    # - example:
        # def example_function(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
        #     pass

        
# Example:
def example_function(*args, **kwargs):
    '''This function accepts a variable number of positional and keyword arguments.'''
    print('Positional arguments:', args)
    print('Keyword arguments:', kwargs)

# calling the function with different arguments
example_function(1, 2, 3, name='John', age=25)
example_function('hello', 'world', greeting='Hi', language='Python')


# ==================================================================================================
# Function in python:
    # - A function is a block of code that performs a specific task.
    # - Functions are used to organize code into reusable blocks that can be called multiple times.
    # - example:

def greet(name):
    '''This function takes a name as an argument and prints a greeting message.'''
    print(f'Hello, {name}!')

# calling the function
greet('John')
greet('Alice')
greet('Bob')

#excersice:
# 1. Write a Python function that takes a number as an argument and returns the square of that number.
