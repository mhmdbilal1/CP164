"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-03-01"
-------------------------------------------------------
"""
# Imports
from List_linked import List

list1 = List()
list2 = List()


for value in [1, 3, 5, 7]:
    list1.append(value)

for value in [2, 4, 5, 6, 7]:
    list2.append(value)

union_list = List()

union_list.union_r(list1, list2)

print("Union List 1 and List 2:")
current = union_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
