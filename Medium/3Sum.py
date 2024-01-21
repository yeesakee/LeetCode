from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort to avoid duplicates
        nums.sort()

        result = []
        for i, n in enumerate(nums):
            if i == 0 or n != nums[i-1]:
                l, r = (i + 1), (len(nums) - 1)
                while l < r:
                    total = n + nums[l] + nums[r]
                    if total == 0:
                        result.append([n, nums[l], nums[r]])
                        l += 1

                        # keep iterating until we find a number that is not a duplicate
                        while (nums[l] == nums[l-1] and l < r):
                            l += 1
                    elif total > 0:
                        r -= 1
                    else:
                        l += 1
        return result

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)

# [-4, -1, -1, 0, 1, 2]
