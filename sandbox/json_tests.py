# json_tests.py
#
# This program works out how to handle different states you may encounter
# loading a json file that contains a dictionary of settings.
#
# by: Keith Kay

import json

filename = 'testing.json'
my_dict = {}

# first open the the file and determine if it is empty
try:
    with open(filename, 'r') as file_obj:
        if file_obj.read():
            # The file is not empty
            print("I read something")
            # The seek(0) is need because the 'read()'above has moved the file
            # cursor to EOF, so we need to move it back
            file_obj.seek(0)
            my_dict = json.load(file_obj)
            test_value_1 = my_dict['test_value_1']
            print(test_value_1)
        else:
            # The file exists, but has nothing in it
            print("I read nothing")
            with open(filename, 'w') as file_obj:
                my_dict = {'test_value_1': '0'}
                json.dump(my_dict, file_obj)
            
except FileNotFoundError:
    print("File doesn't exist")
    # Create the file and write the dict
    with open(filename, 'w') as file_obj:
        my_dict = {'test_value_1': '0'}
        json.dump(my_dict, file_obj)
        
except KeyError:
    print("File exists, but key not found")
    # File exists but the key was not in the dict
    with open(filename, 'r+') as file_obj:
        my_dict = json.load(file_obj)
        file_obj.seek(0)
        file_obj.truncate()
        my_dict['test_value_1'] = '0'
        json.dump(my_dict, file_obj)
