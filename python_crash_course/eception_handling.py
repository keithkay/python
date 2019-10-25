# Python Crash Course
#
# Chapter 10 - Exception handling with 'try'

print("Enter two numbers, and I will divide them")
print("(Enter 'q' to quit.)")

# use 'try, exept, else' to handle potential exceptions
while True:
    first_number = input("\nWhat is you first number?: ")
    print("f_n type: ", type(first_number))
    if first_number == 'q':
        break
    second_number = str(input("\nWhat is you second number?: "))
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero dummy!")
    else:
        print(answer)
    
# Exception handling for files
filename = 'nosuchfile.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "\nSorry, the file " + filename + " does not exist."
    print(msg)
    # you can use 'pass' instead to fail silently instead
