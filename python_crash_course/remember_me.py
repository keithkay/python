# Python Crash Course
#
# Chapter 10 - json for storing user data
#
# This program will load the user name and greet the user
# if their name has been stored previously, otherwise it
# will prompt for the name

import json
filename = 'username.json'
username = ''

def get_username():
    """Get the username if it is already in the username.json file."""
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def prompt_username():
    """Prompt for a new username."""
    username = input("Please enter your first name, so that I may greet you: ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    """Greet the user by their name."""
    username = get_username()
    if username:
        
        while True:
            print("Are you " + username + "?")
            same_user = input("Enter Y or N: ")
            
            if same_user.lower() == 'y':
                print("Welcome back, " + username + "!")
                break
            elif same_user.lower() == 'n':
                username = prompt_username()
                print("Your name has been updated, " + username)
                break
            else:
                print("Sorry that response doesn't make sense. Please try again.")
    else:
        username = prompt_username()
        print("I'll remember you next time, " + username + "!")
        
greet_user()