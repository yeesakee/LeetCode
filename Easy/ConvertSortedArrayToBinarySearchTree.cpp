/*
Given an integer array nums where the elements are sorted in ascending order, convert
it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
every node never differs by more than one.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:
Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
*/

#include <vector>
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
        TreeNode* sortedArrayToBSTHelper(vector<int>& nums, int left, int right) {
            if (left > right) {
                return nullptr;
            }
            int mid = (left + right) / 2;
            TreeNode* root = new TreeNode(nums[mid]);
            TreeNode* left_node = sortedArrayToBSTHelper(nums, left, mid - 1);
            TreeNode* right_node = sortedArrayToBSTHelper(nums, mid + 1, right);
            root->left = left_node;
            root->right = right_node;
            return root;
        }
        TreeNode* sortedArrayToBST(vector<int>& nums) {
            return sortedArrayToBSTHelper(nums, 0, nums.size() - 1);
        }
};