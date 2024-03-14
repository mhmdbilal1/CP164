"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt
from utilities import array_to_queue


q = Queue()
lst = [1, 2, 3, 4, 5]
print("List:", lst)
array_to_queue(q, lst)
a1, a2 = queue_split_alt(q)
print("Target1:")
for i in a1:
    print(f"{i}", end='')
print()
print('Target2:')
for i in a2:
    print(f"{i} ", end='')
