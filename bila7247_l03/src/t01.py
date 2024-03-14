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
from utilities import array_to_queue
from Queue_array import Queue
# Constants
queue = Queue()
source = [1, 2, 3, 4, 5]
array_to_queue(queue, source)
for value in queue:
    print(value)
