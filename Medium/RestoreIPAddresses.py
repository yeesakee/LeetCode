# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
# "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that
# can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s.
# You may return the valid IP addresses in any order.

# Example 1:
    # Input: s = "25525511135"
    # Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
    # Input: s = "0000"
    # Output: ["0.0.0.0"]
# Example 3:
    # Input: s = "101023"
    # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
# Constraints:
    # 1 <= s.length <= 20
    # s consists of digits only.

from typing import List
class Solution:

    # Function uses backtracking to find all possible IP Addresses from the string given
    #   s = given string to build IP Addresses
    #   i = index of s currently exploring
    #   curr = current IP Address we're building
    #   subcurr = sub segment of IP Address currently building
    #   count = count of subsgements we have added to curr (4 segments make an IP Address subcurr.subcurr.subcurr.subcurr)
    #   result = stores all valid IP Addresses found
    def backtracking(self, s, i, curr, subcurr, count, result):
        # if length of curr == length of (s) + 3 (for 3 dots in IP Address) and count == 4 then
        # we've found a valid IP Address
        if len(curr) == len(s) + 3 and count == 4:
            result.append(curr)
            
        # if count == 4 or i >= len(s) that means IP Address is invalid
        if count == 4 or i >= len(s):
            return
        
        # check for leading 0 (cannot have values such as '02')
        if not(len(subcurr) > 0 and int(subcurr) == 0):
            subcurr += s[i]
            
        dot = ""
        # if subcurr is greater than 255 then stop exploring this substring and return
        if int(subcurr) <= 255:
            dot = "." if len(curr) > 0 else ""
        else:
            return
        i += 1
        self.backtracking(s, i, curr + dot + subcurr, "", count + 1, result)
        self.backtracking(s, i, curr, subcurr, count, result)
        return


    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtracking(s, 0, "", "", 0, result)
        return result