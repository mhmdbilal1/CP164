"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports

# Constants


from Queue_circular import Queue

cq, target = Queue(3), Queue(3)
lst = [1, 2, 3]
ls = [3, 1, 2]

print(f"Empty before: {cq.is_empty ()}")
print(f"Full before: {cq.is_full ()}")
print(f"length before: {len(cq)}")
print(f"Equal before: {cq == target}")
print(f"List: (1st)")
for l in lst:
    cq.insert(1)
for l in ls:
    target.insert(1)
print("Inserting list:")
for v in cq:
    print(v)
print(f"Empty after: {cq.is_empty()}")
print(f"Full after: {cq.is_full()}")
print(f"length after: {len(cq)}")
print(f"Equal after: {cq == target}")
print(f"Peek: {cq.peek()}")
print("Removing list:")
for _ in range(len(cq)):
    print(cq.remove())
