# Python Crash Course
#
# Chapter 10 - json handling

  

numbers = [2,3,4,5,6,11,13]

# first we will write out to a json file
filename= 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
    
# now read it into a different list
new_numbers = []
with open(filename, ) as file_object:
    new_numbers = json.load(file_object)

print (new_numbers)
