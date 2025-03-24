# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:19:13 2025

@author: Mehrshad
"""

words = ["Python", "is", "awesome"]
result = ""

for word in words:
    result += word[0]
    print(f"this is {result}")

print(result)

# =============================================================================
# breeking the loops statement
    # pass: does nothing
    # break: exits the loop
    # continue: skips the rest of the code inside the loop for the current iteration

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        pass
    print(i)

# =============================================================================
### operator of % which is called modulo operator and pronounced as mod operator
# returns the remainder of the division of the number to the left by the number on its right
# =============================================================================
# list comprehension
# define a list and then use it to create another list
# [expression for item in list] 
# or [expression for item in list if conditional] 
# or [expression if else for item in list]
# or [expression if else for item in list if conditional]
# or [expression for item in list for item2 in list2]
# or [expression for item in list for item2 in list2 if conditional]

# example:

numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers]
print(squared)

# example 2:
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers if number > 2]
print(squared)

# example 3:
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 if number > 2 else number ** 3 for number in numbers]
print(squared)

# example 4:
numbers = [1, 2, 3]
numbers2 = [4, 5]
squared = [number * number2 for number in numbers for number2 in numbers2]
print(squared)

# example 5:
numbers = [1, 2, 3]
numbers2 = [4, 5]
squared = [number * number2 for number in numbers for number2 in numbers2 if number2 > 4]
print(squared)
# is equal to:
squared = []
for number in numbers:
    for number2 in numbers2:
        if number2 > 4:
            squared.append(number * number2)
print(squared)

# =============================================================================
# lambda functions
# a small anonymous function
# lambda arguments: expression
# example:
add = lambda x, y: x + y
print(add(5, 3))

# =============================================================================
# special functions
    # range()
    # enumerate()
    # zip()

for i in range(1,6):
    for j in range(1,6):
        print(i, j, i*j, end="\t")
    print() # to print in new line to present in a table format

list1 = ["eat", "sleep", "repeat"]
for i, j in enumerate(list1):
    print(i, j)

#example of zip:
list1 = ["eat", "sleep", "repeat"]
list2 = ["apple", "banana", "cherry"]
price = ["45", "67", "98"]
for pack in zip(list1, list2, price):
    print(pack)
# ouput is a tuple of the corresponding elements from the lists:
# ('eat', 'apple', '45')
# without zip it can be done as:

for i in range(len(list1)):
    print(list1[i], list2[i], price[i]) 
    # to make it tuple we can use tuple() function:
    print(tuple((list1[i], list2[i], price[i])))


# =============================================================================