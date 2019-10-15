# Python Crash Course
#
# Chapter 7 Example use of the modulo operator '%'

number = input("Give me a number, and I will tell you if it is odd or even: ")
number = int(number)

# modulo returns the remainder from a division operation, and since even
# numbers are by definition divisible by 2, so if the modulo of a number
# and 2 is zero, the number is even
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")