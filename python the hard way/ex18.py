#ex18.py

# define function to print arguements
def print_two(*args):
    arg1, arg2 = args
    print(f"argi: {arg1}, arg2: {arg2}")

# another function doing the same thing
def print_two_again(arg1, arg2):
    print(f"argi: {arg1}, arg2: {arg2}")

# one that take only one arguement
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguement
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("zed","Shaw")
print_one("First!")
print_none()
