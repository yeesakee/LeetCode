# 86. Partition List
# Given the head of a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
    # Input: head = [1,4,3,2,5,2], x = 3
    # Output: [1,2,2,4,3,5]
# Example 2:
    # Input: head = [2,1], x = 2
    # Output: [1,2]

# Constraints:
    # The number of nodes in the list is in the range [0, 200].
    # -100 <= Node.val <= 100
    # -200 <= x <= 200

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = None
        # store the partition node where the next node < x will be moved to (next of part node)
        part = None
        while(curr != None):
            if curr.val < x:
                # if there are no previous nodes then update part and continue
                if prev == None:
                    part = curr
                else:
                    # if part has not been initialized make head the part node
                    if part == None:
                        prev.next = curr.next
                        curr.next = head
                        part = curr
                        head = curr
                    else:
                        prev.next = curr.next
                        curr.next = part.next
                        part.next = curr
                        part = curr
            prev = curr
            curr = curr.next
        return head

