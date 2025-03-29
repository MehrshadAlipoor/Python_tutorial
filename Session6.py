# Date: 2025/03/28 & 29
# ====================================================================================
# # 1. Oop in Python:
#     # - OOP stands for Object-Oriented Programming.
#     # - OOP is a programming paradigm that uses objects and classes to organize code.
#     # - OOP is based on the concept of encapsulation, inheritance, and polymorphism.
#     # - OOP allows for code reusability and modularity.
#     # - OOP is widely used in modern programming languages, including Python, Java, C++, and Ruby.

# # 2. what is a class?
#     # - A class is a blueprint for creating objects.
#     # - A class defines the properties and behaviors of an object.
#     # - A class can have attributes (data members) and methods (functions).
#     # - A class can be instantiated to create objects. it is a template for creating objects.
#     # - An instance means an object created from a class with specific values for its attributes.
#     # -    example: if we have a class called "Car", 
#            we can create an instance of that class called "my_car" with specific values for its attributes like color, make, and model. 
#     # -    my_car = Car(color='red', make='Toyota', model='Camry')

# # what is an object?
#     # - An object is an instance of a class.
#     # - An object has its own state and behavior.
#     # - An object is created from a class.
#     # - An object can access the attributes and methods of its class.
#     # - An object can be created by calling the class name followed by parentheses. i,e, class_name().
#     # -    example: if we have a class called "Car",
#            we can create an object of that class called "my_car" with specific values for its attributes like color, make, and model.
#     # -    my_car = Car(color='red', make='Toyota', model='Camry')
#     # -    my_car is an object of the class Car.
#     # - Everything in Python is an object. That's why Python is called an object-oriented programming language.

# # what is an attribute?
#     # - An attribute is a variable that is defined inside a class.
#     # - An attribute is used to define the properties of an object.
#     # - An attribute can be accessed using the dot notation. i,e, object_name.attribute_name.
#     # - Methods are usually defined after the attributes in a class.
#     # - An attribute can be defined using the self keyword followed by the attribute name and value. i,e, self.attribute_name = value.
#     # -    example: if we have a class called "Car",
#            we can define attributes like color, make, and model that define the properties of the car.

# # what is a method?
#     # - A method is a function that is defined inside a class.
#     # - A method is used to define the behavior of an object.
#     # - A method can access the attributes of the class.
#     # - A method can be called on an object to perform a specific action.
#     # - A method is defined using the def keyword followed by the method name and parentheses. i,e, def method_name(self, args).
#     # - The first parameter of a method is **always** self, which refers to the instance of the class.
#     # -    example: if we have a class called "Car",
#            we can define a method called "start_engine" that starts the engine of the car.

class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(
            f'The engine of the {self.color} {self.brand} {self.model} is started.')


# # creating an object of the class Car
my_car = Car(color='red', brand='Toyota', model='Camry')

# # calling the method start_engine on the object my_car
my_car.start_engine()

# # what is a constructor?
#     # - A constructor is a special method that is called when an object is created from a class. like __init__ method.
#     # - __init__ is a special method that is called when an object is created from a class.
#     # - __init__ is used because of the following reasons:
#         # - It allows you to initialize the attributes of the class when an object is created.
#         # - It allows you to set default values for the attributes of the class.
#         # - It allows you to perform any setup or initialization that is required for the object.
#     # - A constructor is defined using the def keyword followed by the method name __init__ and parentheses. i,e, def __init__(self, args).
#     # - The first parameter of a constructor is always self, which refers to the instance of the class.
#     # - A constructor can have any number of parameters, but the first parameter must always be self. like the following example:
#         # class Car:
#         #     def __init__(self, color, brand, model):
#         #         self.color = color
#         #         self.brand = brand
#         #         self.model = model

# # what does self mean? and why is it used?
#     # - self is a reference to the current instance of the class.
#     # - self is used to access the attributes and methods of the class.
#     # - self is used to differentiate between instance variables and local variables.
#     # - local variables are variables that are defined inside a method.
#     # - instance variables are variables that are defined inside a class.
#     # - instance variables are defined using the self keyword. i,e, self.variable_name = value.
#     # - local variables are defined without the self keyword. i,e, variable_name = value.
#     # - local variables are only accessible inside the method where they are defined.


# # what is encapsulation?
#     # - Encapsulation is the process of wrapping data and methods into a single unit called a class.
#     # - Encapsulation is used to hide the internal implementation details of a class from the outside world.
#     # - Encapsulation is used to protect the data and methods of a class from being accessed or modified by outside code.
#     # - Encapsulation is achieved using access modifiers like public, private, and protected. 
#     # - example:

class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age    

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age
# # creating an object of the class Person
my_person = Person(name='John', age=25)
# # accessing the private attributes using the getter methods
print(my_person.get_name())  # Output: John
print(my_person.get_age())   # Output: 25
# # modifying the private attributes using the setter methods
my_person.set_name('Jane')
my_person.set_age(30)
# # accessing the private attributes using the getter methods
print(my_person.get_name())  # Output: Jane
print(my_person.get_age())   # Output: 30
# # accessing the private attributes directly will raise an error
# print(my_person.__name)  # AttributeError: 'Person' object has no attribute '__name'
# # accessing the private attributes using the getter methods
# print(my_person.get_name())  # Output: John
# # accessing the private attributes using the getter methods
# print(my_person.get_age())   # Output: 25


# # what is inheritance?
#     # - Inheritance is a mechanism that allows a class to inherit the properties and methods of another class.
#     # - Inheritance allows for code reusability and modularity. 
#     # - Inheritance allows for the creation of a new class that is based on an existing class. 
#     # - example: 
#         # if we have a class called "Animal" that has properties like species and age,
#         # we can create a new class called "Dog" that inherits the properties and methods of the class "Animal".
#         # The class "Dog" can have its own properties and methods in addition to the properties and methods of the class "Animal".

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def make_sound(self):
        print(f'The {self.species} makes a sound.')

# # creating an object of the class Animal
my_animal = Animal(species='Dog', age=5)
# inheriting the class Animal in the class Dog
class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age) # calling the constructor of the parent class Animal
        # super() is used to call the constructor of the parent class.
        # super() is used to access the methods and properties of the parent class.
        # instead of using super() you can also use the name of the parent class to call the constructor of the parent class.
        # i,e, Animal.__init__(self, species, age)
        self.breed = breed

    def make_sound(self):
        print(f'The {self.species} barks.')

# # what happens if a class inherits from multiple classes?
#     # - If a class inherits from multiple classes, it is called multiple inheritance.
#     # - Multiple inheritance allows a class to inherit the properties and methods of multiple classes.
#     # - Multiple inheritance can lead to ambiguity if two parent classes have methods with the same name.
#     # - In Python, the method resolution order (MRO) is used to determine the order in which the methods are called.
#     # - The MRO is determined by the order in which the classes are defined in the class definition. it uses as follows:
#         # class A:
#         #     pass
#         # class B:
#         #     pass
#         # class C:
#         #     pass
#         # class D(A, B, C):
#         pass
#         # class E(B, C):
#         #     pass
# example of using MRO:
class A:
    def method(self):
        print('Method of class A')

class B:
    def method(self):
        print('Method of class B')

class C:
    def method(self):
        print('Method of class C')

class D(A, B, C):
    pass

class E(B, C):
    pass

# # creating an object of the class D
my_object_d = D()
# # calling the method of the class D
my_object_d.method()  # Output: Method of class A
# # creating an object of the class E
my_object_e = E()
# # calling the method of the class E
my_object_e.method()  # Output: Method of class B
# as you can see the method of class D is called from class A and the method of class E is called from class B.
# # this is because of the MRO. The MRO is determined by the order in which the classes are defined in the class definition.

# # what is polymorphism?
#     # - Polymorphism is the ability of an object to take on many forms.
#     # - Polymorphism allows for the creation of methods that can be used with different types of objects.
#     # - An example of polymorphism is the use of the same method name in different classes like the following example:
class Dog:
    def make_sound(self):
        print('Woof!')


class Cat:
    def make_sound(self):
        print('Meow!')



# # creating an object of the class Dog
my_dog = Dog()
# # creating an object of the class Cat
my_cat = Cat()
# # calling the method make_sound on the object my_dog
my_dog.make_sound()  # Output: Woof!
# # calling the method make_sound on the object my_cat
my_cat.make_sound()  # Output: Meow!
# # as you can see the same method name make_sound is used in different classes Dog and Cat.
# # this is an example of polymorphism. The same method name is used in different classes with different implementations.
# # this is also an example of method overriding. 
# # Method overriding is the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.
#     # - Method overriding is a feature of OOP that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
#     # - Method overriding allows a subclass to provide its own implementation of a method that is already defined in its superclass.
#     # - Method overriding is used to change the behavior of a method in a subclass.


# # what is abstract class?
#     # - An abstract class is a class that cannot be instantiated.
#     # - An abstract class is a class that contains one or more abstract methods.
#     # - An abstract method is a method that is declared but does not have an implementation.
#     # - An abstract class is used to define a common interface for a group of related classes.
#     # - An abstract class is used in the following scenarios:
#         # - When you want to define a common interface for a group of related classes. like the following example:
#         # - Imagine you have a class called "Shape" that has an abstract method called "area".
#         # - You can create subclasses of the class "Shape" like "Circle", "Square", and "Triangle" that implement the "area" method in their own way.
#         # - This allows you to define a common interface for all shapes, while still allowing each shape to have its own implementation of the "area" method.
#         # - This is an example of polymorphism, where the same method name is used in different classes with different implementations.
#         # - When you want to define a common interface for a group of related classes, but you don't want to create an instance of the abstract class.
#         # - When you want to define a common interface for a group of related classes, but you want to enforce that the subclasses implement the abstract methods.
#         # - like for example file handling, where you want to define a common interface for file handling classes and you want to enforce that the subclasses implement the abstract methods as below:
class FileHandler(ABC):
    @abstractmethod
    def open_file(self, file_name):
        pass


    @abstractmethod
    def read_file(self):
        pass


    @abstractmethod
    def write_file(self, data):
        pass

#     # - The FileHandler class is an abstract class that defines a common interface for file handling classes.
#     # - The open_file, read_file, and write_file methods are abstract methods that do not have an implementation.
#     # - The subclasses of the FileHandler class must implement the open_file, read_file, and write_file methods.
#     # - The subclasses of the FileHandler class can be used to create file handling classes that implement the open_file, read_file, and write_file methods.



#     # - An abstract class is defined using the abc module in Python. an example of an abstract class is as follows:

from abc import ABC, abstractmethod # importing the ABC and abstractmethod classes from the abc module
#     # - The ABC class is used to define an abstract class.

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    ## - An abstract class can have concrete methods (methods with implementation) in addition to abstract methods.
#     # - A concrete method is a method that has an implementation.
#     # - A concrete method can be called on an object of the class.
#     # - A concrete method is defined using the def keyword followed by the method name and parentheses. i,e, def method_name(self, args).
#     # - A concrete method can access the attributes and methods of the class.

# ==========================================================================================================================
# magic methods or special methods or dunder methods:
#     # - Magic methods are special methods that are defined in a class.
#     # - Magic methods are used to define the behavior of a class when it is used with certain operators or functions.
#     # - Magic methods are defined using the double underscore (__) before and after the method name. i,e, __method_name__.
#     # - Magic methods are also called dunder methods (double underscore methods).
#     # - Magic methods are used to define the behavior of a class when it is used with certain operators or functions.

# List of magic methods:
#     # - __init__(self, args): constructor method, called when an object is created from a class.
#     # - __str__(self): called when the str() function is called on an object of the class.
#     # - __repr__(self): called when the repr() function is called on an object of the class. it returns a string representation of the object.
#     # - Diffrerence between __str__ and __repr__:
#         # - __str__ is used to define a string representation of an object that is user-friendly and easy to read.
#         # - __repr__ is used to define a string representation of an object that is unambiguous and can be used to recreate the object.
# example of __str__ and __repr__:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __repr__(self):
        return f'Person({self.name}, {self.age})'
    
#instance of the class Person:
person = Person(name='John', age=25)
# # calling the str() function on the object person
print(str(person))  # Output: Person(name=John, age=25)
# # calling the repr() function on the object person
print(repr(person))  # Output: Person(John, 25)

#     # - __len__(self): called when the len() function is called on an object of the class.
#     # - __del___(self): called when an object is deleted.
