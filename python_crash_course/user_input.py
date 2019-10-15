# Python Crash Course
#
# Chapter 7 Examples

# the 'input()' function is used to get user input
message = input("Give me something to repeat: ")
print(message)

# user input using this is always captured as a string, so if you actually need
# an integer, convert it using 'int()'
name = input("What's your name?: ")
age = input("And, what is your age " + name + "?: ")
age = int(age)