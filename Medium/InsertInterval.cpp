/*
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by
starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

** Return intervals after the insertion. **

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]
Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 
Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
*/

#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    bool check_interval_overlap(vector<int> interval, vector<int> newInterval) {
        return (newInterval[0] <= interval[0] && newInterval[1] <= interval[1] && newInterval[1] >= interval[0]) ||
                (newInterval[0] >= interval[0] && newInterval[1] >= interval[1] && newInterval[0] <= interval[1]);
    }
    
    bool check_interval_absorb(vector<int> interval, vector<int> newInterval) {
        return (newInterval[0] <= interval[0] && newInterval[1] >= interval[1] || 
                interval[0] <= newInterval[0] && interval[1] >= newInterval[1]);
    }
    
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> result;
        int index = 0;
        // base case, if intervals is empty or newInterval can be inserted at index 0
        if (intervals.size() == 0) {
            result.insert(result.begin(), newInterval);
            return result;
        }
        // loop through intervals and only add intervals that do not overlap
        for (int i = 0; i < intervals.size(); i++) {
            // check if current interval overlaps with newInterval
            if (!check_interval_overlap(intervals[i], newInterval) &&
                !check_interval_absorb(intervals[i], newInterval)) {
                // add intervals that come before newInterval
                if (intervals[i][1] < newInterval[0]) {
                    result.insert(result.begin() + index, intervals[i]);
                    index++;
                }
                // since intervals is sorted, if current interval is greater than newInterval
                // add newInterval to result then add the rest of the intervals to result
                else {
                    result.insert(result.begin() + index, newInterval);
                    result.insert(result.end(), intervals.begin() + i, intervals.end());
                    return result;
                }
            }
            // adjust interval we want to add according to overlapping intervals
            else {
                if (intervals[i][0] < newInterval[0]) {
                    newInterval[0] = intervals[i][0];
                }
                if (intervals[i][1] > newInterval[1]) {
                    newInterval[1] = intervals[i][1];
                }
            }
        }
        // add newInterval to the end of result
        result.insert(result.end(), newInterval);
        return result;
    }
};