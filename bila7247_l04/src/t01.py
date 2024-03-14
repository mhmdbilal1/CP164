"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-01"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list
from List_array import List

# Constants
llist = List()
source = [1, 2, 3, 4, 5]
array_to_list(llist, source)
for i in range(len(llist)):
    print(llist[i])
