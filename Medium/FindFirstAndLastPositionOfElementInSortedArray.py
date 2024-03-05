# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]
# Example 2:
    # Input: nums = [5,7,7,8,8,10], target = 6
    # Output: [-1,-1]
# Example 3:
    # Input: nums = [], target = 0
    # Output: [-1,-1]
 
# Constraints:
    # 0 <= nums.length <= 105
    # -109 <= nums[i] <= 109
    # nums is a non-decreasing array.
    # -109 <= target <= 109
    
from typing import List

class Solution:

    # search the starting position of the element (left most target value in the array)
    def searchStart(self, nums, target):
        l, r = 0, len(nums) - 1

        while (l <= r):
            m = (l + r) // 2

            # if nums[m] == target and m == 0 then that means starting index must be 0, can't go further left
            # if nums[m] == target and nums[m-1] != target that means index m is the left most target number
            if (nums[m] == target and m == 0) or (nums[m] == target and nums[m-1] != target):
                return m
            
            # if nums[m] == target and nums[m-1] == target that means m is not the left most target
            # if nums[m] > target that means that the target is on the left side of the array
            # both cases shift r = m - 1 to continue searching left array
            elif nums[m] == target and nums[m-1] == target or nums[m] > target:
                r = m - 1
            # otherwise the target must be on the right side of the array, update l = m + 1
            else:
                l = m + 1
        return -1

    # search the ending position of the target (right most target value in the array)
    def searchEnd(self, nums, target):
        l, r = 0, len(nums) - 1

        while (l <= r):
            m = (l + r) // 2

            if (nums[m] == target and m == len(nums) - 1) or (nums[m] == target and nums[m+1] != target):
                return m
            elif nums[m] == target and nums[m+1] == target or nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    # given nums sorted in non-decreasing order
    # return starting and ending position of given target value [start, end]
    # if target value not found return [-1, -1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchStart(nums, target), self.searchEnd(nums, target)]