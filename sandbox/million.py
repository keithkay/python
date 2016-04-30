# lets see how long it takes to generate and print from 1 to a million

million = list(range(1,1000001))
for number in million:
	print number

print("Lets check we have all the numbers")
print("minimum = " + str(min(million)))
print("maximum = " + str(max(million)))
print("And the sum of a million is " + str(sum(million)))