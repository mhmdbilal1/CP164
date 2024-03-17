"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports

# Constants
from BST_linked import BST


print("--__eq__--")
bst = BST()

for val in [11, 24, 67, 25, 73, 13]:
    bst.insert(val)

print("BST 1 contents: ")
for i in bst:
    print(i)

bst2 = BST()

for val in [12, 1, 36, 54, 24]:
    bst2.insert(val)

print("BST 2 contents: ")
for k in bst2:
    print(k)

print(" ")

print("Are both BSTs equal? ", bst == bst2)

print(" ")
print("--is_balanced--")
b = bst.is_balanced()
print("Is BST balanced? ", b)

print(" ")
print("--is_valid--")
b = bst.is_valid()
print("Is BST valid? ", b)

print(" ")
print("--min--")
value = bst.min()
print("Min value in BST: ", value)

print(" ")
print("--leaf_count--")
count = bst.leaf_count()
print("Number of leaves in BST: ", count)

print(" ")
print("--one_child_count--")
count = bst.one_child_count()
