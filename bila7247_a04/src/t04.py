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
from utilities import array_to_queue


q = Queue()
lst = [1, 2, 3, 4, 5]
print("List: ", lst)
array_to_queue(q, lst)
t1, t2 = q.split_alt()
print("Target1:")
for v in t1:
    print(f" {v} ", end='')
print()
print("Target2:")
for v in t2:
    print(f"{v} ", end='')
