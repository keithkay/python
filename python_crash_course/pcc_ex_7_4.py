# Python Crash Course
#
# Exercise 7-4

toppings = []
active = True
prompt = "\nPlease enter one topping at a time."
prompt += "\nEnter 'Q' to stop entering toppings: "

print("Welcome to PizzaBot, I'll be taking your order!")

while active:
    new_topping = input(prompt)

    if new_topping.lower() == 'q':
        active = False
    else:
        toppings.append(new_topping)
        print("Got it! " + new_topping + " added!")

print("\nAlright, pizza with ")

for topping in toppings:
    print(topping + " ")

print("coming up!")