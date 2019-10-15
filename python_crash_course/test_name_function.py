# Python Crash Course
#
# Chapter 11 - Testing
#
# This is the unit test to test name_function.py

import unittest
from name_function import format_this_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    # each test must be named test_...
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = format_this_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amedeus Mozart' work?"""
        formatted_name = format_this_name('wolfgang', 'mozart', 'amedeus')
        self.assertEqual(formatted_name, 'Wolfgang Amedeus Mozart')
        
    
    
unittest.main()