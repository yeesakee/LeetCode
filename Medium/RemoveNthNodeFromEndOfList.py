# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]
# Example 2:
    # Input: head = [1], n = 1
    # Output: []
# Example 3:
    # Input: head = [1,2], n = 1
    # Output: [1]

# Constraints:
    # The number of nodes in the list is sz.
    # 1 <= sz <= 30
    # 0 <= Node.val <= 100
    # 1 <= n <= sz


from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        s = []
        currNode = head
        while currNode != None:
            s.append(currNode)
            currNode = currNode.next
        
        currNode = s.pop()
        rightNode = None
        for _ in range(n-1):
            rightNode = currNode
            currNode = s.pop()
        
        leftNode = head
        if len(s) > 0:
            leftNode = s.pop()
            leftNode.next = rightNode
        else:
            head = rightNode
    
        return head