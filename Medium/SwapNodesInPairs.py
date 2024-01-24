# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)

# Example 1:
    # Input: head = [1,2,3,4]
    # Output: [2,1,4,3]

# Example 2:
    # Input: head = []
    # Output: []

# Example 3:
    # Input: head = [1]
    # Output: [1]
 

# Constraints:
    # The number of nodes in the list is in the range [0, 100].
    # 0 <= Node.val <= 100
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, n):
        nextNode = n.next
        if nextNode == None:
            return n
        else:
            n.next = nextNode.next
            nextNode.next = n
        return nextNode

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        head = self.swapNodes(head)
        if head.next != None and head.next.next != None:
            prevN = head.next
            while prevN != None and prevN.next != None:
                currN = self.swapNodes(prevN.next)
                prevN.next = currN
                if currN != None and currN.next != None:
                    prevN = prevN.next.next
                else:
                    break
        return head