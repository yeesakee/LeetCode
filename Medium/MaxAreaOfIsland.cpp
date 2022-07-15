/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid
are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.
** Return the maximum area of an island in grid. If there is no island, return 0 **

Example 1:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
*/

#include <vector>
using namespace std;

class Solution {
    public:
        int getArea(vector<vector<int>>& grid, int curr_row, int curr_column) {
            vector<int> row = {-1, 1, 0, 0};
            vector<int> column = {0, 0, -1, 1};
            int total = 0;
            if (curr_row >= 0 && curr_column >= 0 && curr_row < grid.size() && curr_column < grid[0].size()) {
                if (grid[curr_row][curr_column] == 1) {
                    total++;
                    grid[curr_row][curr_column] = 0;
                    for (int i = 0; i < 4; i++) {
                        total += getArea(grid, curr_row + row[i], curr_column + column[i]);
                    }
                }
                else {
                    return 0;
                }
            }
            return total;
        }
        int maxAreaOfIsland(vector<vector<int>>& grid) {
            int curr = 0;
            int greatest = 0;
            for (int i = 0; i < grid.size(); i++) {
                for (int j = 0; j < grid[i].size(); j++) {
                    if (grid[i][j] == 1) {
                        curr = getArea(grid, i, j);
                        if (curr > greatest) {
                            greatest = curr;
                        }
                    }
                }
            }
            return greatest;
        }
};