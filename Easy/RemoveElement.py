# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        try:
            size = count
            for i in range(size):
                print(str(nums))
                nums.remove(val)
                count -=1
        except ValueError:
            pass
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums=nums, val=2))