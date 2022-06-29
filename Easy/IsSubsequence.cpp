/*
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

** Given two strings s and t, return true if s is a subsequence of t, or false otherwise **

Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
*/

#include <iostream>

using namespace std;

class Solution {
    public:
        bool isSubsequence(string s, string t) {
            // want to loop through the string that has the longer length
            // and store it in string t
            if (t.length() == 0 && s.length() == 0) {
                return true;
            }
            int index_s = 0;
            for (int i = 0; i < t.length(); i++) {
                if (s[index_s] == t[i]) {
                    index_s++;
                }
            }
            if (index_s < s.length()) {
                return false;
            }
            return true;
        }
};
