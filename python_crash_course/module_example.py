# Python Crash Course
#
# Chapter 8 Modules

import pizza

pizza.make_pizza('pepperoni')

# if you don't want to have to type 'pizza.' for every function call
# you can do a few different things

# from pizza import *
# or
# from piza import make_pizza

# you can also give an alias to the module or a function within it
# import pizza as p
# from pizza import make_pizza as mp
#
# which can be called
# p.make_pizza('topping')
# mp('topping')