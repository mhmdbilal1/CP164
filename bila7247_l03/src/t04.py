"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_pq
from Queue_array import Queue
# Constants
pq = Queue()
source = [1, 2, 3, 4, 5]
array_to_pq(pq, source)

for value in pq:
    print(value)
