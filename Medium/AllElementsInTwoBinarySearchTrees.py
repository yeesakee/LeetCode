# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Example 1:
    # Input: root1 = [2,1,4], root2 = [1,0,3]
    # Output: [0,1,1,2,3,4]
# Example 2:
    # Input: root1 = [1,null,8], root2 = [8,1]
    # Output: [1,1,8,8]

# Constraints:
    # The number of nodes in each tree is in the range [0, 5000].
    # -105 <= Node.val <= 105

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getElementsFromBST(self, root):
        result = []
        if root != None:
            result.extend(self.getElementsFromBST(root.left))
            result.append(root.val)
            result.extend(self.getElementsFromBST(root.right))
        return result
    
    def combineTreeList(self, tree1, tree2):
        result = []
        i1 = 0
        i2 = 0
        while(i1 < len(tree1) or i2 < len(tree2)):
            if i1 >= len(tree1):
                result.extend(tree2[i2:])
                return result
            if i2 >= len(tree2):
                result.extend(tree1[i1:])
                return result
            
            if tree1[i1] <= tree2[i2]:
                result.append(tree1[i1])
                i1 += 1
            else:
                result.append(tree2[i2])
                i2 += 1
        
        return result
            

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree1 = self.getElementsFromBST(root1)
        tree2 = self.getElementsFromBST(root2)
        return self.combineTreeList(tree1, tree2)
        