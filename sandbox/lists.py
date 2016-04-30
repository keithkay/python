# python lists

# use purals for list names

bicycles = ['trek', 'cannondale','redline','specialized'] #brackets signify this is a list
print(bicycles) 		# prints the representation of the list, not a formatted list

for bike in bicycles:	# prints a nice list
	print bike

# accessing specific items in the list

print(bicycles[0])		# first
print(bicycles[-1])		# last item

names = ['tom', 'bill', 'jane']
names.append('sue')		# add an item to the end of a list
print(names)
print('\n')


# build a list of numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []				# declare  list
for value in range(1,11):	# generate numbers 1-10
	squares.append(value**2)

print(squares)

# or use a list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)