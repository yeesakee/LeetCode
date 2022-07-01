/*
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Example 2:
    Input: root = [1]
    Output: [[1]]

 Example 3:
    Input: root = []
    Output: []
*/
#include <vector>
#include <set>
#include <iterator>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        set<TreeNode*> s;
        set<TreeNode*> s2;
        vector<vector<int>> result;
        s.insert(root);
        set<TreeNode*>::iterator itr;
        if (root == nullptr) {
            return result;
        }
        while(!s.empty()) {
            vector<int> v;
            for (itr = s.begin(); itr != s.end(); itr++) {
                if ((*itr) != nullptr) {
                    if ((*itr)->left != nullptr) {
                    TreeNode* left = (*itr)->left;
                    s2.insert(left);
                    }
                    if ((*itr)->right != nullptr) {
                        TreeNode* right = (*itr)->right;
                        s2.insert(right);
                    }
                    v.push_back((*itr)->val);
                }
                s.erase(itr);
            }
            result.push_back(v);
            s.swap(s2);
        }
        return result;
    }
};