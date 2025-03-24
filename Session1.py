# Description: This file contains the code for the first session of the Python course with Jadi
# Date: 18/3/2025

person = {"name": "Ali", "age": 25}
print(person["name"])
print(person["age"])

person["city"] = "Tehran"
#to address a specific key in a dictionary
print(person.get("name"))
#to address a specific value in a dictionary using slicing
print(person.get("name")[0])
print(person.values())
#get method is used to get the value of a specific key in a dictionary

# =============================================================================
# set 
# set is a collection of unique elements
# set is unordered and unindexed
# set is mutable so we can add or remove elements from it
# set is defined by curly braces
# set is used to perform mathematical operations
# set is used to remove duplicates from a list
# set is used to check if an element is in a set

my_set = {1,2,3,3,3,4,5}
print(my_set)
my_set.add(11)
print(my_set)

# set methods
# add() method is used to add an element to a set
# remove() method is used to remove an element from a set
    # example: my_set.remove(3)
# discard() method is used to remove an element from a set
#   example: my_set.discard(3)
# the difference between remove and discard is that remove raises an error if the element is not found in the set
# but discard does not raise an error if the element is not found in the set
# difference() method is used to return the difference between two sets
#   example: my_set.difference(your_set)
# union() method is used to combine two sets
#   example: my_set.union(your_set)
# clear() method is used to remove all elements from a set
# copy() method is used to copy a set
# pop() method is used to remove the last element from a set
#   example: my_set.pop()
set_test=set()
set_test.add(1)
set_test.add(2)
set_test.add(3)
print(set_test)
my_set.union(set_test)
print(my_set)
print(my_set.difference(set_test))
print(my_set.pop())
print(my_set)
print(my_set.intersection(set_test))

# =============================================================================
# None data type
# None data type is used to define a null value or no value at all
# None data type is used to define a variable without a value
# None data type is used to define a function that does not return a value
# None data type is not the same as 0 or an empty string
# None data type is a data type of its own
# None data type is a keyword in Python

print(type(None))
print(False)

# =============================================================================
# file I/O
# file I/O is used to read and write files in Python
    # file I/O is used to store data in a file
    # file I/O is used to read data from a file
    # file is data type in Python and can be read and written
    # file is opened using the open() function

# file modes
    # r: read a file
    # a: append to a file
    # w: write to a file
    # x: create a file
    # t: text mode
    # b: binary mode => used to read and write binary files
    # +: read and write => opens a file for reading and writing
    # r+: read and write => opens a file for reading and writing
    # w+: write and read => opens a file for writing and reading

# file methods
    # read(): reads a file
    # readline(): reads a line of a file
    # write(): writes to a file
    # close(): closes a file
    # open(): opens a file
    # seek(): sets the file's current position
        # example: file.seek(0) sets the file's current position to the beginning of the file
    # tell(): returns the file's current position 
        # example: file.tell() returns the file's current position 
    # readlines(): reads all lines of a file
    # readline method reads a line of a file
    
    



