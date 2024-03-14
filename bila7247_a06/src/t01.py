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
from Queue_linked import Queue
# Constants
queue1 = Queue()
queue2 = Queue()
queue3 = Queue()

for i in range(1, 6):
    queue1.insert(i)
for i in range(6, 11):
    queue2.insert(i)

print(f"Queue1 is empty: {queue1.is_empty()}")
print(f"Queue2 is empty: {queue2.is_empty()}")

print(f"front of Queue1: {queue1.peek()}")
print(f"front of Queue2: {queue2.peek()}")

print(f"Removed from Queue1: {queue1.remove()}")
print(f"Removed from Queue2: {queue2.remove()}")

queue3.combine(queue1, queue2)
print("Elements in Queue3 after combining Queue1 and Queue2:")
for value in queue3:
    print(value, end="")
print()

queue1, queue2 = queue3.split_alt()
print("Elements in Queue1 after splitting Queue3:")
for value in queue1:
    print(value, end="")
print()

print("Elements in Queue2 after splitting Queue3:")
for value in queue2:
    print(value, end="")
print()
print(f"length of Queue1: {len(queue1)}")
print(f"length of Queue2: {len(queue2)}")
queue1._append_queue(queue2)

print("Elements in Queue1 after appending Queue2:")
for value in queue1:
    print(value, end="")
print()
new_queue = Queue()
new_queue.insert(1)
print(f"Is Queue1 equal to a new_queue{queue1 == new_queue}")

new_queue._append_queue(queue1)
print(f"Queue1 equal to new_queue after appending?{queue1 == new_queue}")
