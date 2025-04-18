#Date: 2025-04-17
# # ==========================================================
# Advanced Python Madules

# You can find their list in standard library documentation.
# https://docs.python.org/3/library/index.html

# collections:
#     # A module that provides specialized container datatypes.
#     # It includes namedtuple, deque, Counter, OrderedDict, defaultdict, and ChainMap.
#     # These data structures are more efficient and provide additional functionality compared to built-in types.
#     # For example, Counter is a dictionary subclass for counting hashable objects, and defaultdict provides a default value for missing keys.
#     # Example:
#         from collections import Counter, defaultdict
#         # Counter example
#         my_list = ['apple', 'banana', 'apple', 'orange']
#         counter = Counter(my_list)
#         print(counter)  # Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
#         # defaultdict example
#         my_dict = defaultdict(int)
#         my_dict['apple'] += 1
#         my_dict['banana'] += 2
#         print(my_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
#

# dque:
#     # A double-ended queue that allows adding and removing elements from both ends efficiently.
#     # It is useful for implementing queues and stacks.
#     # Example:
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4)  # Add to the right end
my_deque.appendleft(0)  # Add to the left end
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
my_deque.pop()  # Remove from the right end
print(my_deque)  # Output: deque([0, 1, 2, 3])
my_deque.popleft()  # Remove from the left end
print(my_deque)  # Output: deque([1, 2, 3])

# namedtuple:
#     # A factory function for creating tuple subclasses with named fields.
#     # It improves code readability and allows accessing fields by name instead of index.
#     # Example:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x)  # Output: 10
print(point.y)  # Output: 20
#
# Counter:
#     # A dictionary subclass for counting hashable objects.
#     # It is useful for counting occurrences of elements in a collection.
#     # Example:
from collections import Counter
my_list = ['apple', 'banana', 'apple', 'orange']
counter = Counter(my_list)
print(counter)  # Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
#
# Defaultdict:
#     # A dictionary subclass that provides a default value for missing keys.
#     # It is useful for avoiding KeyErrors when accessing missing keys.
#     # Example:
from collections import defaultdict
my_dict = defaultdict(int)
my_dict['apple'] += 1
my_dict['banana'] += 2
print(my_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
#
# itertools:
#     # A module that provides functions for creating iterators for efficient looping.
#     # It includes functions for creating infinite iterators, combinatorial generators, and more.
#     # Example:
from itertools import count, cycle, repeat

# Infinite iterator example
counter = count(start=10, step=2)  # Start from 10 and increment by 2
for _ in range(5):
    print(next(counter))  # Output: 10, 12, 14, 16, 18

# Cycle example
#     # Cycle through a list indefinitely
my_list = ['A', 'B', 'C']
cycler = cycle(my_list)
for _ in range(6):
    print(next(cycler))  # Output: A, B, C, A, B, C

# Repeat example
#     # Repeat a value indefinitely
repeater = repeat('Hello', times=3)  # Repeat 'Hello' 3 times
for value in repeater:
    print(value)  # Output: Hello, Hello, Hello
#     # Note: The repeat function has a times parameter to limit the number of repetitions.
#     # If you want to repeat indefinitely, you can omit the times parameter.
#     # Example:
repeater = repeat('Hello')
for _ in range(3):
    print(next(repeater))  # Output: Hello, Hello, Hello
#     # Be careful with infinite iterators, as they can lead to infinite loops if not handled properly.
#     # Always use a break condition or limit the number of iterations when using infinite iterators.

# =============================================================
# Datetime:
#     # A module for manipulating dates and times.
#     # It provides classes for working with dates, times, and intervals.
#     # Example:
from datetime import datetime, timedelta
# Get the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)
# Get the current date
current_date = current_datetime.date()
print("Current date:", current_date)
# Get the current time
current_time = current_datetime.time()
print("Current time:", current_time)
# Create a specific date and time
specific_datetime = datetime(2023, 4, 17, 12, 30, 0)  # Year, Month, Day, Hour, Minute, Second
print("Specific date and time:", specific_datetime)
# Calculate the difference between two dates
date1 = datetime(2023, 4, 17)
date2 = datetime(2023, 4, 20)
date_difference = date2 - date1
print("Date difference:", date_difference.days, "days")
# Add a time interval to a date
time_interval = timedelta(days=5, hours=3, minutes=30)
new_date = date1 + time_interval
print("New date after adding interval:", new_date)
# Format a date as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)
# Parse a date string into a datetime object
date_string = "2023-04-17 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)
#     # Note: The datetime module provides various formatting options for displaying dates and times.
#     # You can refer to the official documentation for more details on formatting options:
#     # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
#     # Example:

formatted_date = current_datetime.strftime("%A, %B %d, %Y")
print("Formatted date:", formatted_date)  # Output: Monday, April 17, 2023
#     # This formats the date as "Day of the week, Month Day, Year".
#     # You can customize the format string to display the date in different ways.
#     # For example, you can use "%d/%m/%Y" to display the date as "Day/Month/Year".
#     # Example:
formatted_date = current_datetime.strftime("%d/%m/%Y")
print("Formatted date:", formatted_date)  # Output: 17/04/2023
#     # The datetime module also provides functions for parsing date strings into datetime objects.
#     # You can use the strptime function to convert a date string into a datetime object.
#     # Example:
date_string = "2023-04-17 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed date:", parsed_date)  # Output: 2023-04-17 12:30:00
#     # This converts the date string into a datetime object using the specified format.
#     # You can customize the format string to match the format of the date string you are parsing.
#     # For example, if the date string is in the format "Day/Month/Year", you can use "%d/%m/%Y" as the format string.
#     # Example:
date_string = "17/04/2023"
parsed_date = datetime.strptime(date_string, "%d/%m/%Y")
print("Parsed date:", parsed_date)  # Output: 2023-04-17 00:00:00
#     # This converts the date string into a datetime object using the specified format.
#     # You can also include time information in the date string and format string.
#     # Example:
date_string = "17/04/2023 12:30:00"
parsed_date = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
print("Parsed date:", parsed_date)  # Output: 2023-04-17 12:30:00
#     # This converts the date string into a datetime object with both date and time information.
#     # The datetime module provides various formatting options for displaying dates and times.
#     # You can refer to the official documentation for more details on formatting options:
#     # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# ==========================================================

# math:
#     # A module that provides mathematical functions and constants.
#     # It includes functions for trigonometry, logarithms, exponentiation, and more.
#     # Example:
import math
# Calculate the square root of a number
sqrt_value = math.sqrt(16)
print("Square root of 16:", sqrt_value)  # Output: 4.0
# Calculate the sine of an angle (in radians)
sin_value = math.sin(math.pi / 2)  # Sine of 90 degrees (pi/2 radians)
print("Sine of 90 degrees:", sin_value)  # Output: 1.0
# Calculate the cosine of an angle (in radians)
cos_value = math.cos(math.pi)  # Cosine of 180 degrees (pi radians)
print("Cosine of 180 degrees:", cos_value)  # Output: -1.0
# Calculate the tangent of an angle (in radians)
tan_value = math.tan(math.pi / 4)  # Tangent of 45 degrees (pi/4 radians)
print("Tangent of 45 degrees:", tan_value)  # Output: 1.0
# Calculate the logarithm of a number (base 10)
log_value = math.log10(100)  # Logarithm of 100 (base 10)
print("Logarithm of 100 (base 10):", log_value)  # Output: 2.0
# Calculate the exponent of a number
#     # Exponentiation (e^x)
exp_value = math.exp(2)  # e^2
print("e^2:", exp_value)  # Output: 7.38905609893065
#     # Note: The math module provides various mathematical functions and constants.
#     # You can refer to the official documentation for more details on available functions and constants:
#     # https://docs.python.org/3/library/math.html
#     # Example:
# Calculate the value of pi
pi_value = math.pi
print("Value of pi:", pi_value)  # Output: 3.141592653589793
# Calculate the value of e (Euler's number)
e_value = math.e
print("Value of e:", e_value)  # Output: 2.718281828459045
# Calculate the factorial of a number
#     # Factorial of 5 (5!)
factorial_value = math.factorial(5)
print("Factorial of 5:", factorial_value)  # Output: 120

# ==========================================
# random:
#     # A module for generating random numbers and performing random operations.
#     # It includes functions for generating random integers, floating-point numbers, and selecting random elements from sequences.
#     # Example:
import random
# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)
# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)
# Generate a random floating-point number between a specified range (1.5 to 5.5)
random_uniform = random.uniform(1.5, 5.5)
print("Random float between 1.5 and 5.5:", random_uniform)
# Select a random element from a list
my_list = ['apple', 'banana', 'orange']
random_choice = random.choice(my_list)
print("Random choice from the list:", random_choice)
# Shuffle a list randomly
my_list = ['apple', 'banana', 'orange']
random.shuffle(my_list)
print("Shuffled list:", my_list)  # Output: Randomly shuffled list
#     # Note: The random module provides various functions for generating random numbers and performing random operations.
#     # You can refer to the official documentation for more details on available functions:
#     # https://docs.python.org/3/library/random.html
#     # Example:
# Generate a random sample from a population
population = ['A', 'B', 'C', 'D', 'E']
sample_size = 3
random_sample = random.sample(population, sample_size)
print("Random sample from the population:", random_sample)  # Output: Random sample of size 3 from the population
#     # This selects 3 random elements from the population without replacement.
#     # The sample function is useful for selecting a subset of elements from a larger population.
#     # You can specify the sample size and the population from which to select the sample.
#     # Note: If you want to select random elements with replacement, you can use the choices function.

#     # Example:
# Select random elements with replacement
random_choices = random.choices(population, k=3)
print("Random choices with replacement:", random_choices)  # Output: Random choices of size 3 from the population
#     # This selects 3 random elements from the population with replacement.
#     # The choices function allows you to specify the number of elements to select (k) and can include duplicates in the selection.
#     # You can also specify weights for the elements to influence the selection probability.
# Simulate rock-paper-scissors game
#     # Example:
def play_rps():
    choices = ['rock', 'paper', 'scissors']
    user_choice = random.choice(choices)
    computer_choice = random.choice(choices)
    print("User choice:", user_choice)
    print("Computer choice:", computer_choice)
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        print("User wins!")
    else:
        print("Computer wins!")
    #     # This simulates a simple rock-paper-scissors game where the user and computer make random choices.
    #     # The program determines the winner based on the choices made.
#     # You can run this function to play the game multiple times.
play_rps()

# ==========================================