'''
---------------------------------------------------------------------------------------------------
Description:
   Sort a linked list in O(n log n) time using constant space complexity.

Comments:
   Use merge sort (in place - merging linked lists).
   Use runner technique to find the middle of the linked list. The runner technique
   means that you iterate through the linked list with two pointers simultaneously, with one ahead of the
   other. The "fast" node will be hopping two nodes for each one node that the "slow" node iterates through.
   Then split the linked list at half and recursively call merge() on both
   linked lists. Merge using a basic merge() function on the two linked lists.
   O(n log n) time
   O(1) space
---------------------------------------------------------------------------------------------------
'''
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self # start from the head node
        while node != None:
            print node.val # access the node value
            node = node.next # move on to the next node

def sort_list(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head.next.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    halfway_node = slow.next
    slow.next = None
    return merge(sort_list(head), sort_list(halfway_node))

def merge(list1, list2):
    head = tail = Node(0)
    while list1 or list2:
        if list1 is not None:
            if (list2 and list1.val <= list2.val) or list2 is None:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
        if list2 is not None:
            if (list1 and list2.val <= list1.val) or list1 is None:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
    return head.next
