#
# My Functions File
#
# Contains several Python functions for personal use that I have found
# handy.
#
# by: Keith Kay

def format_list(list):
    """Returns the contents of a list in a comma-delimited string """
    return_string = ''
    for item in list:
        return_string = return_string + item + ", "

    #strip the last comma and space
    return_string = return_string[:(len(return_string)-2)]

    return return_string
