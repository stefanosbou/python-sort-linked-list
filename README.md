# Python sort single Linked list
Sort a linked list in O(n log n) time using constant space complexity

**example usage:** 
```python
>>> from sort_linked_list import Node, sort_list
>>> node1 = Node(37)
>>> node2 = Node(99)
>>> node3 = Node(12)
>>> node1.next = node2
>>> node2.next = node3
>>>
>>> node = sort_list(node1)
>>> node.traverse()
12
37
99
```
