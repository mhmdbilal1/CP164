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
from functions import stack_combine
# Constants
target_stack = Stack()
source1_stack = Stack()
source2_stack = Stack()


source1_stack.push(1)
source1_stack.push(2)
source1_stack.push(3)

source2_stack.push(4)
source2_stack.push(5)
source2_stack.push(6)


target_stack.combine(source1_stack, source2_stack)

while not target_stack.is_empty():
    print(target_stack.pop())
