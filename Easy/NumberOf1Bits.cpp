/*
Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight).

Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:
    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 
Constraints:
    The input must be a binary string of length 32.
*/

#include <string>
#include <bitset>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        string s = bitset<32>(n).to_string();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char temp = s[i];
            int t = (int)temp - 48;
            if (t == 1) {
                count++;
            }
        }
        return count;
    }
};