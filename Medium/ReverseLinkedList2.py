
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]
# Example 2:
    # Input: head = [5], left = 1, right = 1
    # Output: [5]

# Constraints:
    # The number of nodes in the list is n.
    # 1 <= n <= 500
    # -500 <= Node.val <= 500
    # 1 <= left <= right <= n

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # one rotation solution
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if left == right then no reversing is needed
        if left == right:
            return head

        # node before the rotation
        l = None
        curr = head
        prev = None
        i = 1
        while(curr != None):
            # if i == left then we found the node before rotation
            if i == left:
                l = prev
            # if i is within left and right then start rotating nodes
            if i >= left and i <= right:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                # if i == right finish the reversing by modifying
                # last rotated node to be pointed by l
                # and first rotated node to point to node after rotation
                if i == right:
                    # if l == None that means we modify head to store
                    # last rotated node
                    if l == None:
                        head.next = curr
                        head = prev
                    else:
                        # first rotated node will always be l.next
                        # since l stores node before rotation
                        l.next.next = curr
                        l.next = prev
                    break
            else:
                prev = curr
                curr = curr.next
            i += 1
        return head
    
    
    # solution that finds the left and right node then rotates them

    # given linkedlist rotate nodes count times from left.next node
    # def reverseList(self, head, left, prev, right, count):
    #     curr = head if left == None else left.next
    #     prev = None
    #     while curr != None and count >= 0:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #         count -= 1

    #     if left == None:
    #         head.next = right
    #         head = prev
    #     else:
    #         left.next.next = right
    #         left.next = prev
        
    #     return head
            

    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if left == right:
    #         return head
        
    #     l = head
    #     r = head
    #     prev = None
    #     i = 1
    #     while r != None:
    #         if i == left:
    #             l = prev
    #         if i == right:
    #             prev = r
    #             r = r.next
    #             return self.reverseList(head, l, prev, r, right - left)
    #         prev = r
    #         r = r.next
    #         i += 1
    #     return head
