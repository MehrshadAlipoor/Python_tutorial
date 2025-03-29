## Animal Management System in Zoo with oop:

class Animal:
    def __init__ (self, name, species, age, sound, zoo_name):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name
        
    def make_sound(self):
        print(f'{self.name} the {self.species} says {self.sound}!')

    def info(self):
        print(f'{self.name} is a {self.age} year old {self.species} in {self.zoo_name}.')

    def __str__(self): # This method returns a string representation of the animal info
        return f'{self.name} the {self.species} is {self.age} years old and lives in {self.zoo_name}. It says {self.sound}.'
    

class bird(Animal):
    def __init__ (self, name, species, age, sound, zoo_name, wing_span):
        super().__init__(name, species, age, sound, zoo_name)
        self.wing_span = wing_span
        
    def make_sound(self):
        print(f'{self.name} chirps {self.sound}!')

    def fly(self):
        print(f'{self.name} is flying with a wingspan of {self.wing_span} meters!') 


# instantiate the Animal class
lion = Animal('Leo', 'Lion', 5, 'Roar', 'Safari Park')
lion.info() # This will call the info method
lion.make_sound() # This will call the make_sound method
print(lion) # This will call the __str__ method

# instantiate the bird class
sparrow = bird('Sparky', 'Sparrow', 2, 'Chirp', 'City Zoo', 0.25)
sparrow.info() # This will call the info method
sparrow.fly() # This will call the fly method
sparrow.make_sound() # This will call the make_sound method
print(sparrow) # This will call the __str__ method