# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]

# Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
 

# Constraints:
#   2 <= nums.length <= 104
#   -109 <= nums[i] <= 109
#   -109 <= target <= 109
#   Only one valid answer exists.

from typing import List
import copy

class Solution:
    # better run-time
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in numToIndex:
                return [numToIndex[remainder], i]
            numToIndex[nums[i]] = i

    #  better memory
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     nums_len = len(nums)
    #     sorted_list = nums.copy()
    #     sorted_list.sort()

    #     for i in range (nums_len):
    #         remainder = target - sorted_list[i]
    #         for j in range(i+1, nums_len):
    #             if sorted_list[j] == remainder:
    #                 num1 = nums.index(sorted_list[i])
    #                 num2 = nums.index(sorted_list[j])
    #                 if num2 == num1:
    #                     nums.remove(sorted_list[i])
    #                     num2 = nums.index(sorted_list[j])+1
    #                 return [num1, num2]
    #             if sorted_list[j] > remainder:
    #                 break

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(nums = [7,2,11,15], target = 9))