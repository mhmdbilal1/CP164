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
from functions import stack_combine
from Stack_array import Stack

# Constants
source1 = Stack()
source2 = Stack()

# Populate the source stacks
source1.push(5)
source1.push(8)
source1.push(12)

source2.push(3)
source2.push(6)
source2.push(1)

# Call the stack_combine function
stack_combine(source1, source2)
