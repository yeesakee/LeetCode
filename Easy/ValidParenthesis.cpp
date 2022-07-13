/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
*/

#include <stack>
#include <string>
using namespace std;

class Solution {
    public:
        bool isValid(string s) {
            stack<char> st;
            for (int i = 0; i < s.length(); i++) {
                char temp = s[i];
                if (temp == '(' || temp == '[' || temp == '{') {
                    st.push(temp);
                }
                if (temp == ')' || temp == ']' || temp == '}') {
                    if (st.empty()) {
                        return false;
                    }
                    char temp_s = st.top();
                    st.pop();
                    if (temp_s + 1 != temp && temp_s + 2 != temp) {
                        return false;
                    }
                }
            }
            if (!st.empty()) {
                return false;
            }
            return true;
        }
};