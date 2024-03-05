# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
    # Input: n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
    # Input: n = 1
    # Output: ["()"]

# Constraints:
    # 1 <= n <= 8
    

from typing import List

class Solution:
    def generateParenthesisHelper(self, curr, open, close, n):
        result = []
        if open == close and open == n:
            return [curr]
        if open < n:
            result.extend(self.generateParenthesisHelper(curr + "(", open + 1, close, n))
        if close < open:
            result.extend(self.generateParenthesisHelper(curr + ")", open, close + 1, n))
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesisHelper("", 0, 0, n)