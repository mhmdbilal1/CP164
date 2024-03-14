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

for value in [1, 2, 3, 4, 5]:
    list1.append(value)
    list2.append(value)

identical = list1.is_identical_r(list2)
print(f"Lists are{' ' if identical else ' not '}identical.")

list2.append(6)
identical = list1.is_identical_r(list2)
print(f"""Adding an element to list 2,lists are 
{' ' if identical else ' not '} identical.
      """)

list3 = List()
for value in [5, 4, 3, 2, 1]:
    list3.append(value)

identical = list1.is_identical_r(list3)
print(f"The lists are{' ' if identical else ' not '}identical.")
