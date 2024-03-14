"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
from utilities import array_to_stack
# Constants
source1 = Stack()
array_to_stack(source1, [3, 6, 1, 7, 9, 14])
print(f"Original values: {source1._values}")
stack_reverse(source1)
print(f"Reversed values: {source1._values}")
