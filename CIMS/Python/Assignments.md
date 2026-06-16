<img width="743" height="488" alt="image" src="https://github.com/user-attachments/assets/5c59f52b-b9a6-48b3-b740-96aaca1c6937" />
Here are concise notes on **Python Collections** and related concepts for quick reading.

# Python Collections Overview

Python provides built-in data structures and the `collections` module for specialized containers.

---

# 1. List (`list`)

* Ordered collection.
* Mutable (can be changed).
* Allows duplicates.
* Indexed.

```python
nums = [1, 2, 3, 2]
```

### Common Operations

```python
append()
insert()
remove()
pop()
sort()
reverse()
```

### Time Complexity

* Access: O(1)
* Append: O(1)
* Insert/Delete middle: O(n)

### Use When

* Need ordered, editable data.

---

# 2. Tuple (`tuple`)

* Ordered.
* Immutable.
* Allows duplicates.
* Faster than lists for fixed data.

```python
point = (10, 20)
```

### Features

```python
count()
index()
```

### Use When

* Data should not change.
* Dictionary keys (if contents are immutable).

---

# 3. Set (`set`)

* Unordered.
* Mutable.
* No duplicates.
* Fast membership testing.

```python
s = {1, 2, 3}
```

### Common Operations

```python
add()
remove()
discard()
union()
intersection()
difference()
```

### Time Complexity

* Search: O(1) average

### Use When

* Removing duplicates.
* Fast lookups.

---

# 4. Frozen Set (`frozenset`)

* Immutable version of set.

```python
fs = frozenset([1, 2, 3])
```

### Use When

* Need immutable sets.
* Set as dictionary key.

---

# 5. Dictionary (`dict`)

* Key-value pairs.
* Mutable.
* Ordered (Python 3.7+).

```python
student = {
    "name": "John",
    "age": 20
}
```

### Common Operations

```python
get()
keys()
values()
items()
update()
pop()
```

### Time Complexity

* Access: O(1)
* Insert: O(1)

### Use When

* Mapping data.
* Fast lookups by key.

---

# Collections Module

```python
from collections import *
```

Provides specialized container datatypes.

---

# 6. Counter

Counts occurrences of elements.

```python
from collections import Counter

c = Counter("banana")
```

Output:

```python
{'a':3, 'n':2, 'b':1}
```

### Useful Methods

```python
most_common()
elements()
update()
```

### Use When

* Frequency counting.
* Word count problems.

---

# 7. defaultdict

Dictionary with default values.

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
```

### Common Defaults

```python
int
list
set
float
```

### Use When

* Avoid checking key existence.

---

# 8. OrderedDict

Dictionary that remembers insertion order.

```python
from collections import OrderedDict
```

⚠ Mostly unnecessary since normal dicts preserve order in modern Python.

### Extra Feature

```python
move_to_end()
```

### Use When

* Need order-specific operations.

---

# 9. deque (Double Ended Queue)

Fast insertion/removal from both ends.

```python
from collections import deque

dq = deque([1,2,3])
```

### Methods

```python
append()
appendleft()
pop()
popleft()
rotate()
```

### Time Complexity

* Both-end operations: O(1)

### Use When

* Queues.
* Sliding window problems.
* BFS algorithms.

---

# 10. ChainMap

Combines multiple dictionaries.

```python
from collections import ChainMap

c = ChainMap(dict1, dict2)
```

### Use When

* Searching through multiple configs/settings.

---

# 11. namedtuple

Tuple with named fields.

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
```

```python
p.name
```

instead of

```python
p[0]
```

### Use When

* Lightweight objects.
* Readable tuples.

---

# 12. UserDict

Wrapper around dictionary.

```python
from collections import UserDict
```

### Use When

* Creating custom dictionary classes.

---

# 13. UserList

Wrapper around list.

```python
from collections import UserList
```

### Use When

* Custom list behavior.

---

# 14. UserString

Wrapper around string.

```python
from collections import UserString
```

### Use When

* Custom string classes.

---

# Queue-Related Collections

## Queue (FIFO)

Using deque:

```python
q = deque()

q.append(10)
q.popleft()
```

First In → First Out

---

## Stack (LIFO)

Using list:

```python
stack = []

stack.append(10)
stack.pop()
```

Last In → First Out

---

# Heap (Priority Queue)

Using `heapq`

```python
import heapq

heap = [4,1,3]
heapq.heapify(heap)
```

### Methods

```python
heappush()
heappop()
heapify()
```

### Use When

* Priority scheduling.
* Dijkstra's algorithm.
* Top K elements.

---

# Array

Using `array` module.

```python
from array import array

arr = array('i', [1,2,3])
```

### Advantage

* More memory efficient than lists.

---

# Quick Comparison

| Collection | Ordered | Mutable | Duplicates |
| ---------- | ------- | ------- | ---------- |
| List       | Yes     | Yes     | Yes        |
| Tuple      | Yes     | No      | Yes        |
| Set        | No      | Yes     | No         |
| Frozenset  | No      | No      | No         |
| Dict       | Yes     | Yes     | Keys No    |

---

# Interview Favorites

Most commonly asked:

1. List vs Tuple
2. Set vs Frozenset
3. Dict vs defaultdict
4. Dict vs OrderedDict
5. Queue vs deque
6. Counter usage
7. namedtuple vs class
8. Heap vs Queue
9. List vs deque
10. Mutable vs Immutable collections

These cover about 90% of collection-related questions in Python interviews and coding rounds.
