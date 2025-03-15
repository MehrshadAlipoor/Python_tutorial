# python with Mosh
# # Date: 10/03/2025

# # ================================================================================================
# Classes and Objects

# what is a class?
# A class is a blueprint for creating objects. 
# An object has properties and methods(functions) associated with it. 
# Almost everything in Python is an object.

class Point:  #pascale naming convention: first letter of each word is capitalized
    def __init__(self, x, y): # constructor = a special method in Python
        self.x = x
        self.y = y
        
    def move(self):
        print("move") # method

    def draw(self):
        print("draw")

point1 = Point(5, 10) # object
point1.draw()
point1.move()
point1.x = 10 # attributes = variables that belong to an object
point1.y = 20 # attributes
print(point1.x)

'''point2 = Point()
point2.x = 1
print(point2.x)'''

# each object is independent of each other
# point1 and point2 are two different objects of the same class
# point1 has its own x and y values, and point2 has its own x value

# class constructor
# a constructor is a special method in Python
# a constructor is called when an object is created
# why use a constructor?
    # to initialize the object with some default values
    # to avoid setting the values of the object after creating it
    # to make the code cleaner
    # to make the code more readable

# How to create a constructor in Python?
    # use the __init__ method    
    # __init__ is a special method in Python
    # __init__ is called when an object is created
    # __init__ is also called a constructor

# self parameter
    # self is a reference to the current object
    # self is the first parameter of any method in a class
    # self is not a keyword in Python, you can use any word instead of self
    # self is a convention, and you should use it

point = Point(10, 20)  # TypeError: Point() takes no arguments
point.x = 11
point.y = 22
print(point.x, point.y)
# how to fix the error?
# add a constructor to the class Point

# ================================================================================================
# Exercise: Create a class Person
# create a class Person with the following attributes:
    # name
    # age
    # city
# methods:
#   talk()
#   that prints "Hello, my name is [name] and I am [age] years old. I live in [city]."


class Person:
    def __init__(self, name, age, city):  
        self.name = name
        self.age = age
        self.city = city

    def talk(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I live in {self.city}.")
# every parameter in a class should be preceded by self
# self is a reference to the current object

person = Person("John", 30, "New York")
person.talk()
bob = Person("Bob", 25, "Los Angeles")
bob.talk()

# ================================================================================================
# Inheritance
# what is inheritance?
    # inheritance is a mechanism in which a new class inherits properties and methods from an existing class
    # the existing class is called the parent class or the base class
    # the new class is called the child class or the derived class

# DRY principle = Don't Repeat Yourself! 
    # inheritance helps us to avoid repeating the same code in multiple classes
    # inheritance helps us to reuse the code

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):  # Dog class inherits from Mammal class
    def bark(self):
        print("bark")

class Cat(Mammal):  # Cat class inherits from Mammal class
    def meow(self):
        print("meow")

dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.meow()

# ================================================================================================
# Modules
# what is a module?
    # a module is a file containing Python code
    # a module can define functions, classes, and variables
    # a module can also include runnable code

# why use modules?
    # to organize the code
    # to make the code more readable
    # to reuse the code
    # to avoid naming conflicts

# how to use a module?
    # use the import keyword to import a module
    # use the module name followed by a dot to access the functions, classes, or variables defined in the module

# =================================================================================================
# This appears to be the end of the file
# No additional code needed here