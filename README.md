# Python sort single Linked list
Sort a linked list in O(n log n) time using constant space complexity.
* Use merge sort (in place - merging linked lists). 
* Use runner technique to find the middle of the linked list. The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node will be hopping two nodes for each one node that the "slow" node iterates through.
* Then split the linked list at half and recursively call merge() on both linked lists. Merge using a basic merge() function on the two linked lists.


> O(n log n) time
>
> O(1) space

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
