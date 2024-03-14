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
from functions import pq_split_key
from utilities import array_to_pq

pq = Priority_Queue()
lst = ['a', 'b', 'c', 'd']
print("List: ", lst)
array_to_pq(pq, lst)
t1, t2 = pq_split_key(pq, 'c')
print("Target1 (with higher priority):")
for i in t1:
    print(f"{i} ", end='')
print()
print("Target2 (with lower priority")
for i in t2:
    print(f"{i} ", end='')
