/*
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true
Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false
 
Constraints:
    The number of nodes in the tree is in the range [1, 1000].
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
    public:
        bool checkSymmetry(TreeNode* left, TreeNode* right) {
            if (left == nullptr && right == nullptr) {
                return true;
            }
            if ((left == nullptr && right != nullptr) || (left != nullptr && right == nullptr) || left->val != right->val) {
                return false;
            }
            return checkSymmetry(left->left, right->right) && checkSymmetry(left->right, right->left);
        }
        bool isSymmetric(TreeNode* root) {
            return checkSymmetry(root->left, root->right);
        }
};