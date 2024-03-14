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
for value in [1, 3, 5, 7, 9]:
    list1.append(value)
for value in [0, 2, 4, 6, 8, 9]:
    list2.append(value)

intersection_list = List()

intersection_list.intersection_r(list1, list2)

print("Intersection list 1 and list 2:")
current = intersection_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()
