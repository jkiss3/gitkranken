import pandas as pd
import numpy as np
import seaborn as sns

a = 18
b = 20
print(a+b)
print("ez a második file.")

class Dog:
    # Constructor (init method)
    def __init__(self, name, breed):
        self.name = name  # Attribute: Name of the dog
        self.breed = breed  # Attribute: Breed of the dog

    # Method to bark
    def bark(self):
        return "Woof! I'm a " + self.breed + " named " + self.name

# Creating an object of the Dog class
my_dog = Dog("Fido", "Pumi")

# Accessing attributes and calling methods
print(my_dog.name)  # Accessing the name attribute
print(my_dog.bark())  # Calling the bark method

