/*
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){}
};

class Solution {
    int maxdepth = 0;
    public:
        void findMaxDepth(TreeNode* root, int depth) {
            if (root != nullptr) {
                depth++;
                if (root->left == nullptr && root->right == nullptr) {
                    if (depth > maxdepth) {
                        maxdepth = depth;
                    }
                }
                else {
                    findMaxDepth(root->left, depth);
                    findMaxDepth(root->right, depth);
                }
            }
        }
        int maxDepth(TreeNode* root) {
            findMaxDepth(root, 0);
            return maxdepth;
        }
};