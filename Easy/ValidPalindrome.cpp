/*
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
*/

#include <string>
#include <stack>
#include<ctype.h>
using namespace std;

class Solution {
    public:
        bool isPalindrome(string s) {
            stack<char> stck;
            string str = "";
            for (int i = 0; i < s.length(); i++) {
                char temp = s[i];
                if (isalpha(temp)) {
                    temp = tolower(temp);
                    stck.push(tolower(temp));
                    str += temp;
                }
                if (isdigit(temp)) {
                    stck.push(temp);
                    str += temp;
                }

            }
            int half = str.length() / 2;
            for (int i = 0; i < half; i++) {
                char temp = stck.top();
                stck.pop();
                if (temp != str[i]) {
                    return false;
                }
            }
            return true;
        }
};