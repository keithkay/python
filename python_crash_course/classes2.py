# Python Crash Course
#
# Chapter 9 OOP

from car_classes import Car, ElectricCar, Battery

# main body
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.descriptive_name())
my_new_car.update_odometer(122)
my_new_car.read_odometer()
print("")

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
print("")

my_tesla = ElectricCar('tesla', 'model s', 2016, 70)
print(my_tesla.descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.get_range()