/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101
 
Constraints:
   0 = n <= 105
*/

#include <vector>
#include <string>
#include <cmath>
using namespace std;

class Solution {
    public:
        vector<int> countBits(int n) {
            vector<int> result;
            result.push_back(0);
            int offset = 1;
            int next_offset = 2;
            for (int i = 1; i <= n; i++) {
                if (i == next_offset) {
                    offset = next_offset;
                    next_offset *= 2;
                }
                result.push_back(1 + result[i - offset]);
            }
            return result;
        }
};