/*
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
of all the values of the nodes in the tree.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1
Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

Constraints:
    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104
*/

#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(): val(0), left(nullptr), right(nullptr){}
    TreeNode(int x, TreeNode *left, TreeNode *right): val(x), left(left), right(right) {}
};

class Solution {
public:
    int kth = 0;
    int kthSmallestValue = 0;
    int kthSmallest(TreeNode* root, int k) {
        if (root != nullptr) {
            if (root->left == nullptr && root->right == nullptr) {
                kth++;
                if (kth == k) {
                    kthSmallestValue = root->val;
                }
            }
            else {
                kthSmallest(root->left, k);
                kth++;
                if (kth == k) {
                    kthSmallestValue = root->val;
                    return kthSmallestValue;
                }
                kthSmallest(root->right, k);
            }
        }
        return 0;
    }
};