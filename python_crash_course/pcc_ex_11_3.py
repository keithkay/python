# Python Crash Course
#
# Chapter 11 - Testing
#
# Employee class for exercise 11-3

class Employee():
    """A simple class to model an employee."""
    
    def __init__(self, fname, lname, salary):
        """Initialize the class by storing the first and last names and salary."""
        self.first_name = fname
        self.last_name = lname
        self.annual_salary = salary
        
    def give_raise(self, amount=5000):
        """Give the employee a raise of $5,000 or the amount specified"""
        self.annual_salary += amount
        print("Cha-ching!")