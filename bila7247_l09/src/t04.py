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

hset = Hash_Set(5)
for i in range(8):
    hset.insert(i)

print("Before rehashing:")
hset.debug()

hset._rehash()

print("\nAfter rehashing:")
hset.debug()
