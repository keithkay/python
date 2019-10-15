# Python Crash Course
#
# Chapter 7 'While' loops

# basic while loop
number = 1
while number <= 5:
    print(number)
    number += 1

# using a while loop to keep a program running until user quits
prompt = "\nGive me something to repeat."
prompt += "\nEnter 'Q' to quit: "

message = ""
active = True

while active:                       # you can also use 'while True' and 'break'
    message = input(prompt)

    if message.lower() != "q":
        print(message)
    else:
        active = False

# 'continue' is used to bypass the rest of the while loop code and return to
# the top of the loop as opposed to 'break' which exits the loop immediately
number = 0
print("\nPrinting some odd numbers.")

while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

# while can also be used with a list or dictionary to keep looping until the
# list or dict is empty
#
# while my_list: