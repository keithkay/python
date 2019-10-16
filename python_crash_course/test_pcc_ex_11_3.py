# Python Crash Course
#
# Chapter 11 - Testing
#
# Unit tests for Employee class in exercise 11-3

import unittest
from pcc_ex_11_3 import Employee

class TestEmployee(unittest.TestCase):
    """A collection of unit test for the Employee class."""
    
    def setUp(self):
        """Create an Employee object and assign initial values"""
        self.fname = 'John'
        self.lname = 'Smith'
        self.salary = 60000
        self.testEmployee = Employee(self.fname, self.lname, self.salary)
        
    def test_give_default_raise(self):
        """Test giving the employee a default raise."""
        self.testEmployee.give_raise()
        self.assertEqual((self.salary + 5000), self.testEmployee.annual_salary)
        
    def test_give_custom_raise(self):
        """Test giving the employee a default raise."""
        custom_raise = 1000
        self.testEmployee.give_raise(custom_raise)
        self.assertEqual((self.salary + custom_raise), self.testEmployee.annual_salary)
        
unittest.main()