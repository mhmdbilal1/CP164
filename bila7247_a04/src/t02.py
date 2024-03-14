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
from Queue_array import Queue
from utilities import array_to_queue

source, target = Queue(), Queue()
list1 = [1, 2, 3]
list2 = [1, 2, 3]
array_to_queue(source, list1)
array_to_queue(target, list2)

print(source == target)
