# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
#   Input: strs = ["flower","flow","flight"]
#   Output: "fl"

# Example 2:
#   Input: strs = ["dog","racecar","car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.
 

# Constraints:
#   1 <= strs.length <= 200
#   0 <= strs[i].length <= 200
#   strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len = len(strs)
        word_index = 0
        min_word_len = len(min(strs, key=len))
        prefix_check = True
        common_prefix = ""

        if min_word_len == 0 or list_len == 0:
            return common_prefix
        
        while prefix_check:
            curr_char = strs[0][word_index]
            for i in range(1, list_len):
                if strs[i][word_index] != curr_char:
                    prefix_check = False
                    break
            if prefix_check:
                common_prefix += curr_char
            word_index += 1
            if word_index == min_word_len:
                prefix_check = False
        return common_prefix

            



if __name__ == "__main__":
    solution = Solution()
    # expected output: "fl"
    print(solution.longestCommonPrefix(strs = ["flower","flow","flight"]))
