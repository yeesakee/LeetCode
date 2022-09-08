/*
Given a sorted array of distinct integers and a target value,

return the index if the target is found. 
If not, return the index

where it would be if it were inserted in order. 
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1
Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
 
Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
*/

#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // edge cases
        if (target <= nums[0]) {
            return 0;
        }
        if (target > nums[nums.size() - 1]) {
            return nums.size();
        }
        return binary_search(nums, 0, nums.size() - 1, target);
    }

    int binary_search(vector<int>& nums, int left, int right, int target) {
        if (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target || (nums[mid] > target && nums[mid - 1] < target)) {
                return mid;
            }
            if (nums[mid] < target && nums[mid + 1] > target) {
                return mid + 1;
            }
            if (nums[mid] > target) {
                return binary_search(nums, left, mid - 1, target);
            }
            return binary_search(nums, mid + 1, right, target);
        }
        return 0;
    }
};