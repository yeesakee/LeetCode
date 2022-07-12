/*
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the
image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally
to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally
to those pixels (also with the same color), and so on. Replace the color of all of
the aforementioned pixels with color.

** Return the modified image after performing the flood fill **

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1)
    (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel
    (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:
    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 
Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 216
    0 <= sr < m
    0 <= sc < n
*/

#include <vector>
#include <queue>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<vector<int> > floodFill(vector<vector<int> >& image, int sr, int sc, int color) {
            queue<vector<int> > pixels;
            vector<int> row = {-1, 1, 0, 0};
            vector<int> column = {0, 0, -1, 1};
            pixels.push({sr, sc});
            int curr_color = image[sr][sc];
            image[sr][sc] = color;
            while (!pixels.empty()) {
                vector<int> curr = pixels.front();
                pixels.pop();
                for (int i = 0; i < row.size(); i++) {
                    int next_row = curr[0] + row[i];
                    int next_column = curr[1] + column[i];
                    if (next_row >= 0 && next_row < image.size() && next_column >= 0 &&
                        next_column < image[0].size() && image[next_row][next_column] == curr_color && image[next_row][next_column] != color) {
                        image[next_row][next_column] = color;
                        pixels.push({next_row, next_column});
                    }
                }
            }
            return image;
        }
};