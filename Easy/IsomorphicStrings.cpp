/*
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

** Return true if isomorphic, false otherwise **
Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false
*/

#include <iostream>
#include <map>
#include <set>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        // store mapping pairs of characters of s -> characters of t
        map<char, char> m;
        // stores which characters in t have already been mapped
        // ensures characters in t are not mapped more than once
        set<char> set_t;
        for(int i = 0; i < s.length(); i++) {
            char cs = s[i];
            char ct = t[i];
            if (m.find(cs) != m.end()) {
                if (m[cs] != ct) {
                    return false;
                }
            }
            else {
                // if a character of s has not been mapped but
                // the character of t has been mapped then return false
                if (set_t.find(ct) != set_t.end()) {
                    return false;
                }
            }
            m.insert(pair<char, char> (cs, ct));
            set_t.insert(ct);
        }
        return true;
    }
};