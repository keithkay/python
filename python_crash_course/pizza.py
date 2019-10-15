# Python Crash Course
#
# Chapter 8 Modules

def make_pizza(*toppings):
    """Print a list of the toppings requested"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)