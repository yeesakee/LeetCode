from typing import List

from pyrsistent import s
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        result = []
        while (left < right and top < bottom):
            # traverse the top and to the right of the matrix
            index = left
            while (index < right):
                result.append(matrix[top][index])
                index += 1
            top += 1
            
             # traverse down on the right most column of the matrix
            index = top
            while (index < bottom):
                result.append(matrix[index][right-1])
                index += 1
            right -= 1
            
            if not (left < right and top < bottom):
                break

            # traverse the bottom to the left of the matrix
            index = right - 1
            while (index >= left):
                result.append(matrix[bottom-1][index])
                index -= 1
            bottom -= 1
            
            # traverse to the top of the left most column of the matrix
            index = bottom - 1
            while (index >= top):
                result.append(matrix[index][left])
                index -= 1
            left += 1
        return result
    
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    s = Solution()
    print(s.spiralOrder(matrix))