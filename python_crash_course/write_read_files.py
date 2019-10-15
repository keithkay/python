# Python Crash Course
#
# Chapter 10 - Write to file

filename = 'programming.txt'

# files are opened with the arguement 'w' to write to them
# note that this will erase the contents of the file if it already
# exists
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    
# use append mode instead to add to it
with open(filename, 'a') as file_object:
    file_object.write("I love gamming too.\n")
