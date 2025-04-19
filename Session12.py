# Date: 25-04-2025
# ===========================================================
# Advanced Madule in Python (cont.)

# Regular Expressions (regex)
    # - A powerful tool for matching patterns in strings.
    # - Used for searching, replacing, and validating strings.
    # - Can be complex, but very useful for text processing.
    # - Python has a built-in module called `re` for regex operations.

# Common Regex Functions in Python
    # - `re.search(pattern, string)`: Searches for the first occurrence of the pattern in the string.
    # - `re.match(pattern, string)`: Checks if the pattern matches at the beginning of the string.
    # - `re.match.group()`: Returns the matched string from the last match.
    # - `re.match.groups()`: Returns all matched groups from the last match.
    # - `re.match.groupdict()`: Returns a dictionary of named groups from the last match.
    # - `re.findall(pattern, string)`: Returns a list of all occurrences of the pattern in the string.
    # - `re.sub(pattern, replacement, string)`: Replaces occurrences of the pattern with the replacement in the string.
    # - `re.replace(pattern, replacement, string)`: Similar to `re.sub`, but returns the number of replacements made.
    # - `re.split(pattern, string)`: Splits the string by the occurrences of the pattern.
    # - `re.compile(pattern)`: Compiles a regex pattern into a regex object for reuse. >>> example: `compiled_pattern = re.compile(r'\d+')`.
    # - `re.escape(string)`: Escapes all non-alphanumeric characters in the string.
    # - `re.finditer(pattern, string)`: Returns an iterator yielding match objects for all occurrences of the pattern in the string.
    # - `re.fullmatch(pattern, string)`: Checks if the entire string matches the pattern.
    # - `re.subn(pattern, replacement, string)`: Similar to `re.sub`, but returns a tuple of the new string and the number of replacements made.
    # - `re.startswith(pattern, string)`: Checks if the string starts with the pattern.
    # - `re.endswith(pattern, string)`: Checks if the string ends with the pattern.


# Example of Regex in Python
import re

# Sample string for regex operations
sample_string = "Hello, my email is sth@sth.it and my phone number is 123-456-7890." 


# Searching for an email address in the string
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_match = re.search(email_pattern, sample_string)
if email_match:
    print(f"Email found: {email_match.group()}")
else:
    print("No email found.")


# Searching for a phone number in the string
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_match = re.search(phone_pattern, sample_string)
if phone_match:
    print(f"Phone number found: {phone_match.group()}")
else:
    print("No phone number found.")


# Common Regex Patterns
    # - `\d`: Matches any digit (0-9).
    # - `\D`: Matches any non-digit character.
    # - `\w`: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore).
    # - `\W`: Matches any non-alphanumeric character.
    # - `\s`: Matches any whitespace character (space, tab, newline).
    # - `\S`: Matches any non-whitespace character.
    # - `{n}`: Matches exactly n occurrences of the preceding element.
    # - `{n,}`: Matches n or more occurrences of the preceding element.
    # - `{n,m}`: Matches between n and m occurrences of the preceding element.
    

# Basic regex syntax
    # - `.`: Matches any character except a newline.
    # - `*`: Matches 0 or more occurrences of the preceding element.
    # - `+`: Matches 1 or more occurrences of the preceding element.
    # - `?`: Matches 0 or 1 occurrence of the preceding element.
    # - `^`: Matches the start of a string.
    # - `$`: Matches the end of a string.
    # - `[]`: Matches any character inside the brackets.
    # - `|`: Acts as a logical OR between expressions.
    # - `()`: Groups expressions together.

# Example of using regex to find all email addresses in a string
text = "Contact us at +150-123-4567 or email us at thisisanemail@email.com or at sample@email.com for more info."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Email addresses found:", emails)

text = "Python is great"
result = re.search(r"\s", text)
print(result.start()) # Output: 6 (index of the first whitespace character)
print(result.end()) # Output: 7 (index of the character after the first whitespace character)


text = "abc 123 def 456"
result = re.findall(r"\d+", text)
print(result)

# ============================================================
# Decimal Module:
    # - The `decimal` module provides support for fast correctly-rounded decimal floating point arithmetic.
    # - It is especially useful for financial applications and other use cases where precision is critical.
    # - The `Decimal` class in the `decimal` module provides a way to represent decimal numbers with arbitrary precision.
    # - It can be used to avoid issues with floating-point arithmetic in Python.
    # - The `decimal` module also provides support for rounding, formatting, and arithmetic operations on decimal numbers.
    # - It is important to note that the `decimal` module is not a replacement for the built-in `float` type, but rather a complement to it.
    # - The `decimal` module is part of the Python standard library and does not require any additional installation.

# Example of using the decimal module
from decimal import Decimal, getcontext


# Set the precision for decimal operations
getcontext().prec = 3
# Create Decimal objects
num1 = Decimal('0.1')
num2 = Decimal('0.2')
num3 = Decimal('0.3')
num4 = Decimal('0.4')


# Perform arithmetic operations
result1 = num1 + num2
result2 = num3 - num4
result3 = num1 * num2
result4 = num3 / num4
result5 = num1 ** num2


# Print the results
print(f"Addition: {result1}")  # Output: 0.3
print(f"Subtraction: {result2}")  # Output: -0.1
print(f"Multiplication: {result3}")  # Output: 0.02
print(f"Division: {result4}")  # Output: 0.75
print(f"Exponentiation: {result5}")  # Output: 0.1^0.2 = 1.0717734625362931
print(f"Precision: {getcontext().prec}")  # Output: 3 (the precision set earlier)
print(f"Decimal representation of 0.1: {num1}")  # Output: 0.1

# what is the difference between Decimal and float?
# - Decimal is a fixed-point representation, while float is a binary floating-point representation.
# - Decimal is more precise for decimal arithmetic, while float is faster for large calculations.
# - Decimal is more suitable for financial applications, while float is more suitable for scientific calculations.

# what if we did not use decimal in previous example?
0.1 + 0.2 == 0.3 # Output: False (due to floating-point precision issues)
0.3 - 0.4 == -0.1 # Output: False (due to floating-point precision issues)
print(0.1 + 0.2) # Output: 0.30000000000000004 (due to floating-point precision issues)
print(0.3 - 0.4) # Output: -0.09999999999999998 (due to floating-point precision issues)
# correct way to compare:
0.1 + 0.2 - 0.3 < 1e-9 # Output: True (within a small tolerance)
# or
# use the decimal module:
Decimal('0.1') + Decimal('0.2') == Decimal('0.3') # Output: True (exact match) 

# what is float precision issue?
# - The float type in Python (and most programming languages) uses binary floating-point representation, which can lead to precision issues when representing decimal numbers.
# - This is because some decimal fractions cannot be represented exactly in binary form, leading to small rounding errors.
# - For example, the decimal number 0.1 cannot be represented exactly in binary, leading to a small error when performing arithmetic operations with it.
# - This can lead to unexpected results when comparing floating-point numbers or performing arithmetic operations with them.







