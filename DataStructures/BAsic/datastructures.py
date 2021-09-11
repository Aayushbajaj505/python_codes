# stacks can be implemeted using lists and by using
# the pop method
# stacks can also be implemeted using list but its not good for performance
# so we use deque as foloow

from collections import deque
from array import array

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

# Arrays
# use only when dealing with large data sets
nums = array("i", [1, 2, 3, 4, 5])

# sets
# nothing can be repeated only unique items
# sets support all the mathematical funcitons
# such as union disjuntion
# items cannot be assesed with index
# unordered collection of items
numbers = [1, 2.3, 4, 5, 6]
first = set(numbers)
