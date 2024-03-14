"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants
deque = Deque()
for value in [1, 2, 3, 4, 5]:
    deque.insert_rear(value)
print("deque after inserting values at rear:")
for values in deque:
    print(value, end="")
print()
for value in [0, -1, -2, -3, -4]:
    deque.insert_front(value)
print("Deque after inserting values at front:")
for value in deque:
    print(value, end=' ')
print()

front_value = deque.remove_front()
rear_value = deque.remove_rear()
print(f"Removed from front: {front_value}, Removed from rear: {rear_value}")

front_peek = deque.peek_front()
rear_peek = deque.peek_rear()
print(f"Peek front: {front_peek}, Peek rear: {rear_peek}")

print("Is the deque empty?", deque.is_empty())

print("Length of the deque:", len(deque))

deque2 = Deque()
for value in [-2, -1, 0, 1, 2, 3, 4]:
    deque2.insert_rear(value)

print("Are deques equal?", deque == deque2)


print("Iterating through the deque:")
for value in deque:
    print(value, end=' ')
print()
