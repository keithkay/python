# Python Crash Course
#
# Chapter 9 OOP

# In order to work with an object in Python, we first need to
# define a class for that object

class Dog():
    """A simple class example"""

    def __init__(self, name, age):
        """Initializes name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('rosey',11)

print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()