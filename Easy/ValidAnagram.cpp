/*
Given two strings s and t.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.

 ** Return true if t is an anagram of s, and false otherwise **

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false
 
Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
*/

#include <string>
#include <map>
using namespace std;

class Solution {
    public:
        bool isAnagram(string s, string t) {
            if (s.length() != t.length()) {
                return false;
            }
            map<char, int> m;
            for (int i = 0; i < s.length(); i++) {
                char temp = s[i];
                m[temp] += 1;
            }
            for (int i = 0; i < t.length(); i++) {
                char temp = t[i];
                if (m.find(temp) == m.end()) {
                    return false;
                }
                if (m[temp] == 1) {
                    m.erase(temp);
                }
                else {
                    m[temp] -= 1;
                }
            }
            return true;
        }
};