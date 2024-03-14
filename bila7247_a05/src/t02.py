"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
# Constants
l1 = Sorted_List()
l2 = Sorted_List()
vals = [1, 2, 3, 4, 5, 7, 8, 9]

for v in vals:
    l1._values.append(v)

b = 4 in l1
print("Contains:", b)
print("Equal:", l1 == l2)
print("Get_item:", l1 == l2)
l2.clean()
print("Clean:", l2._values)
print("Count:", l1.count(1))
print("Find:", l1.find(2))
print("Index:", l1.index(5))

l2._values.append(3)
inter = Sorted_List()
inter.intersection(l1, l2)
print("Intersection:", inter._values)
print("Max:", l1.max())
print("Min:", l1.min())
print("Peek:", l1.peek())
print("Remove:", l2.remove(3))
print("Remove_front:", l1.remove_front())
l1.remove_many(2)
print("Remove_many:", l1._values)
for v in vals:
    l2._values.append(v)

t1, t2 = l2.split()
print("Split:", t1._values, t2._values)
t1, t2 = l2.split_alt()
print("Split_alt:", t1._values, t2._values)
t1, t2 = l1.split_key(2)
print("Split_key:", t1._values, t2._values)
for v in vals:
    l2._values.append(v)
uni = Sorted_List()
uni.union(l1, l2)
print("Union:", uni._values)
