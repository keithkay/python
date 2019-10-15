# Python Crash Course
#
# Chapter 10 - large file example

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print("The first 50 digits of pi are: " + pi_string[:52] + "...")
print("Length check on file: len = " + str(len(pi_string)))