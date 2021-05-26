'''
This code is copied from the base code for the challenge project
found at https://replit.com/github/freeCodeCamp/boilerplate-time-calculator.
It is intended to test the function I created in 'time_calculator.py', using
the 'test_module.py' file.
'''

from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)
