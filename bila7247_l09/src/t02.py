"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-03-14"
-------------------------------------------------------
"""
# Imports

# Constants

from Hash_Set_array import Hash_Set

print("insert:")
hset = Hash_Set(1)
hset.insert(2)
hset.insert(3)
hset.insert(4)
hset.insert(5)

print("Hash set after insert: ")
for i in hset:
    print(i)

print(" ")

print("remove:")

removed = hset.remove(3)

print("Removed value: ", removed)

print("Hash set after remove: ")
for i in hset:
    print(i)
