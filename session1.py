
print("Hello World")

J = 5
print(2+3)
O = 5

students_count = 1000
rating = 4.99
is_published = True
course_name = "  python programming"  # String

print(students_count)

# string methods

print(len(course_name))
print(course_name[-1])
print(course_name[:])

print(course_name.lower())
print(course_name.upper())  # String methods
print(course_name.title())
print(course_name.strip())  # Removes white spaces
# WE have rsstrip() and lstrip() for right and left strip

# Returns the index of the first occurrence of the string
print(course_name.find("mm"))
print(course_name.replace("p", "j"))

print("pro" in course_name)  # Returns a boolean value
# not operator
print("pTo" not in course_name)  # Returns a boolean value


# ================================================================================================
# Numbers
x = 1  # int
y = 1.1  # float
z = 1 + 2j  # complex
print(x)
print(y)
print(z)
#arithmetic operations
print(10 + 3)
print(10 - 3)
print(10 * 3) # Multiplication
print(10 / 3) # Division
print(10 // 3) # Floor division (Rounds down to the nearest whole number)
print(10 % 3) # Modulus (Remainder)
print(10 ** 3) # Exponent (10 to the power of 3)

# Augmented assignment operator
x = 10
x = x + 3
print(x)
x += 3
print(x)

# ================================================================================================
# FUNCTIONS FOR NUMBERS
print(round(2.9))
print(abs(-2.9))    # Absolute value

# ================================================================================================
# math module
import math
print(math.ceil(2.2))
print(math.floor(2.9))
print(math.factorial(5))
print(math.log(10, 10))
print(math.copysign(2, -3))

