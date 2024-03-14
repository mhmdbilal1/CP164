"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq

pq = Priority_Queue()
lst = [1, 2, 3, 4, 5, 6]
print("list: ", lst)
array_to_pq(pq, lst)
t1, t2 = pq.split_key(7)
print("Target1 (with Higher Priority")
for i in t1:
    print(f"{i}", end="")
print()
print("Target2 (with lower Priority")
for i in t2:
    print(f"{i}", end='')
