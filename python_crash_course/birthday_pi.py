# Python Crash Course
#
# Chapter 10 - Birthday Pi

from kay_class import bcolors

# First we load the file and build the string contain the first
# million digits of Pi
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# Next we get the users birthday and use S.find() to return the starting
# index of the birthday in the pi string. S.find() returns -1 if not 
# found.
print(bcolors.BOLD + bcolors.OKBLUE + 
    "\nBirthday Pi!\n" + bcolors.ENDC +
    "Let's find out if your birthday shows up in the "+
    "first million digits of Pi!\n")
birthday = input(
    "Enter your birthday in this format mmddyy or mmddyyyy: ")
position = pi_string.find(str(birthday))

if position == -1:
    print(
        "\nSorry, your birthday does not appear in the first million " +
        "digits of pi.\n")
else:
    print(
        "\nYour birthday appears in Pi, starting at position " + 
        "{0:,d}".format(position))
    print("Let's take a look:\n")
    print("3.141 ... " 
        + pi_string[position-1] + bcolors.MAGNETA
        + pi_string[position:position + len(birthday)] + bcolors.ENDC
        + pi_string[position + len(birthday) + 1] + " ...\n")        
