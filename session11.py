#Date: 2025-04-17
# # ==========================================================
# Advanced Python Madules

# You can find their list in standard library documentation.
# https://docs.python.org/3/library/index.html

# collections:
#     # A module that provides specialized container datatypes.
#     # It includes namedtuple, deque, Counter, OrderedDict, defaultdict, and ChainMap.
#     # These data structures are more efficient and provide additional functionality compared to built-in types.
#     # For example, Counter is a dictionary subclass for counting hashable objects, and defaultdict provides a default value for missing keys.
#     # Example:
#         from collections import Counter, defaultdict
#         # Counter example
#         my_list = ['apple', 'banana', 'apple', 'orange']
#         counter = Counter(my_list)
#         print(counter)  # Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
#         # defaultdict example
#         my_dict = defaultdict(int)
#         my_dict['apple'] += 1
#         my_dict['banana'] += 2
#         print(my_dict)  # Output: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
#

# dque:
#     # A double-ended queue that allows adding and removing elements from both ends efficiently.
#     # It is useful for implementing queues and stacks.
#     # Example:
from collections import deque
my_deque = deque([1, 2, 3])
my_deque.append(4)  # Add to the right end
my_deque.appendleft(0)  # Add to the left end
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
my_deque.pop()  # Remove from the right end
print(my_deque)  # Output: deque([0, 1, 2, 3])
my_deque.popleft()  # Remove from the left end
print(my_deque)  # Output: deque([1, 2, 3])

# namedtuple:
#     # A factory function for creating tuple subclasses with named fields.
#     # It improves code readability and allows accessing fields by name instead of index.
#     # Example:
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point.x)  # Output: 10
print(point.y)  # Output: 20
#
# Counter:
#     # A dictionary subclass for counting hashable objects.
#     # It is useful for counting occurrences of elements in a collection.
#     # Example:
from collections import Counter
my_list = ['apple', 'banana', 'apple', 'orange']
counter = Counter(my_list)
print(counter)  # Output: Counter({'apple': 2, 'banana': 1, 'orange': 1})
#
