# Python Crash Course
#
# Chapter 8 Functions

# functions are defined using 'def'
def greeting(name):
    """Display a simple greeting"""  # this is an example of a docstring
    print("Hello, " + name.title() + "!")

user_name = input("What's your name?: ")
greeting(user_name)

# in addition to the normal positional arguements for a function, you can
# pass 'keyword arguements' to a function, and provide a default for an
# arguement, essentially making it optional (you can also just make it
# optional without a default by using =''
def describe_pet(pet_name, animal_type='cat'):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# now when calling 'describe_pet' we either ensure they are in the correct
# order, or we explictly assign them, illustrated here:
describe_pet('harry', 'hamster')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet('lois')

# functions can also return a value, using, you guessed it 'return'
def format_name(fname, lname, mname=''):
    """Return a full name, neatly formatted."""
    if mname:
        full_name = fname + ' ' + mname + ' ' + lname
    else:
        full_name = fname + ' ' + lname
    return full_name.title()

my_name = format_name('keith', 'kAy')
print(my_name)
print(format_name('J', 'Seymor', 'Thomas'))

# functions can be set up to receive and arbitrary number of arguements
# using '*' tells Python to create a tuple in which to store all the
# arguements received
def make_pizza(*toppings):
    """Print a list of the toppings requested"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# you can also use '**' to pass a dictionary of unknown structure, but
# the dictionary must be passed as keyword-value pairs
def build_profile(fname, lname, **user_info):
    """
    Build a dictionary containing everyting we know about a user.
    """
    profile = {}
    profile['first_name'] = fname
    profile['last_name'] = lname
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print("")
print(user_profile)