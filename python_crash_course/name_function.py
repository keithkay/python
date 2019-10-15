# Python Crash Course
#
# Chapter 11 - Testing
#
# This is the function to be tested by test_name_function.py

def format_this_name(first, last, middle=''):
    """Return a neatly formatted name."""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()