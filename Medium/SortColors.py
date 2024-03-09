# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
    # Input: nums = [2,0,2,1,1,0]
    # Output: [0,0,1,1,2,2]
# Example 2:
    # Input: nums = [2,0,1]
    # Output: [0,1,2]
 
# Constraints:
    # n == nums.length
    # 1 <= n <= 300
    # nums[i] is either 0, 1, or 2.

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        # index
        i = 1
        # index of where to add next red (0)
        # start at -1 if first val of nums is not 0
        r = -1 if nums[0] != 0 else 0
        # index of where to add next white (1)
        w = -1

        while (i < len(nums)):
            # only need to move values to front of list if it is 0 or 1
            # 2 will be left at the end of list
            if nums[i] < nums[i-1]:
                # if the current value is 0
                if nums[i] == 0:
                    # increment the index of where to put the next 0
                    r += 1
                    # increment index of white (1), if we haven't seen a white
                    # leave the index as -1
                    w = w + 1 if w != -1 else -1
                    
                    # remove the current value
                    del nums[i]
                    # insert it back into the list at the right index
                    nums.insert(r, 0)
                elif nums[i] == 1:
                    w = r + 1 if w == -1 else w + 1
                    del nums[i]
                    nums.insert(w, 1)
            # if the value is 0 then we want to increment the red (0) index
            elif nums[i] == 0:
                r = i
            i += 1