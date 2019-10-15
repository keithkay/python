# Python Crash Course
#
# Chapter 10 - working with files

# open a file and print it's contents using 'with', 'open' and 'file_object'
# * open() - opens the file
# * with - closes the file once access is no longer needed
# * file_object - where the contents of the file are stored

file = 'pi_digits.txt'

print("Print the full file:")
with open(file) as file_object:
    contents = file_object.read()
    print(contents)

# use 'rstrip()' to remove the EOF
"""with open(file) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
# now we read line by line instead
print("\nPrinting line by line:")
with open(file) as file_object:
    for line in file_object:
        print(line)               # you could again use rstrip here to
                                  # remove the newlines

# to use the file contents outside of the 'with' block we need to assign
# it to a variable
with open(file) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))