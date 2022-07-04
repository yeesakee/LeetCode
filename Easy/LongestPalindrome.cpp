/*Given a string s which consists of lowercase or uppercase letters,
(letters are case sensitive, for example, "Aa" is not considered a palindrome here)

** Return the length of the longest palindrome that can be built with those letters **

Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.
*/

#include <iostream>
#include <map>
#include <iterator>
using namespace std;

class Solution {
    public:
        int longestPalindrome(string s) {
            map<char, int> m;
            int count = 0;
            for (int i = 0; i < s.length(); i++) {
                char curr = s[i];
                m[curr] += 1;
            }
            map<char, int>::iterator itr;
            for (itr = m.begin(); itr != m.end(); itr++) {
                count += (itr->second / 2) * 2;
            }
            if (count < s.length()) {
                return count + 1;
            }
            return count;
        }
};