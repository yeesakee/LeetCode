# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
    # Input: nums = [1,1,1,2,2,3], k = 2
    # Output: [1,2]
# Example 2:
    # Input: nums = [1], k = 1
    # Output: [1]

# Constraints:
    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104
    # k is in the range [1, the number of unique elements in the array].
    # It is guaranteed that the answer is unique.
 
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterDic = {}
        # create a list of lists of count of max unique nums
        # []        []         []
        # freq 1   freq 2     freq 3
        freqList = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            counterDic[n] = 1 + counterDic.get(n, 0)
        
        # store values based on their frequency
        # example: nums = [1, 1, 1, 2, 2, 3, 4, 5, 5]
        # [3, 4]       [2, 5]       [1]
        # freq 1       freq 2      freq 3
        for key, val in counterDic.items():
            freqList[val].append(key)
        
        # go through freqList from most freq to least and extend to result list
        for i in range(len(freqList) - 1, -1, -1):
            result.extend(freqList[i])
            if len(result) == k:
                return result

        return result


        # first try
        # counterDic = {}
        # minVal = 0
        # result = []

        # # store all values in nums with their count in dictionary
        # for n in nums:
        #     counterDic[n] = 1 + counterDic.get(n, 0)
        
        # for n in counterDic:
        #     # if there are less values in result than k then just add value
        #     if len(result) < k:
        #         result.append(n)

        #         # update minVal if it is the first val or count is less than minVal
        #         if len(result) == 1 or counterDic[n] < counterDic[minVal]:
        #             minVal = n
        #     else:
        #         # if the count of n is greater than minVal in result
        #         if counterDic[n] > counterDic[minVal]:
        #             # remove the minVal from result and add n
        #             result.remove(minVal)
        #             result.append(n)
        #             minVal = n
        #             # loop through result to update minVal
        #             for i in result:
        #                 if counterDic[i] < counterDic[minVal]:
        #                     minVal = i
        
        # return result