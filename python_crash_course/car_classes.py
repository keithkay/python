# Python Crash Course
#
# Chapter 9 OOP

# Class definition for Car
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        """Return a neatly formatted descriptive name."""

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""

        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value, ensuring that
        it isn't reduced.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Reducing the odometer reading is not permitted")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer."""

        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Mileage cannot be negative.")

# Class definition of a car battery
class Battery():
    """A simple model of an electic car battery."""

    def __init__(self, battery_size):
        """Initialize the battery's attributes."""

        self.battery_size = battery_size

        # Set the range based on the battery size.
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 270

    def get_range(self):
        """Print the range of the battery."""

        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)

# Class definition for ElectricCar
class ElectricCar(Car):
    """Represent aspects of a car that are specific to electic vehicles."""
    def __init__(self, make, model, year, battery):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(battery)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This care has a " + str(self.battery.battery_size) + "-kWh battery.")