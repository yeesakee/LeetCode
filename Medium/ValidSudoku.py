# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
    # Input: board = 
    # [["5","3",".",".","7",".",".",".","."]
    # ,["6",".",".","1","9","5",".",".","."]
    # ,[".","9","8",".",".",".",".","6","."]
    # ,["8",".",".",".","6",".",".",".","3"]
    # ,["4",".",".","8",".","3",".",".","1"]
    # ,["7",".",".",".","2",".",".",".","6"]
    # ,[".","6",".",".",".",".","2","8","."]
    # ,[".",".",".","4","1","9",".",".","5"]
    # ,[".",".",".",".","8",".",".","7","9"]]
    # Output: true

# Example 2:
    # Input: board = 
    # [["8","3",".",".","7",".",".",".","."]
    # ,["6",".",".","1","9","5",".",".","."]
    # ,[".","9","8",".",".",".",".","6","."]
    # ,["8",".",".",".","6",".",".",".","3"]
    # ,["4",".",".","8",".","3",".",".","1"]
    # ,["7",".",".",".","2",".",".",".","6"]
    # ,[".","6",".",".",".",".","2","8","."]
    # ,[".",".",".","4","1","9",".",".","5"]
    # ,[".",".",".",".","8",".",".","7","9"]]
    # Output: false
    # Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
    # Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class Solution:

    # board: sudoku board to be checked
    # start_position (x, y): the start position will the the left top corner of the sub-box
    #                        we are checking
    # return: true if sub-box is valid, false otherwise
    def isValidSubBox(self, board: List[List[str]], start_position: tuple()):
        # row and column length of sub-box is 3
        subbox_length = 3
        num_set = set()
        for i in range(0, subbox_length):
            for j in range(0, subbox_length):
                curr_num = board[start_position[0]+i][start_position[1]+j]
                if curr_num.isnumeric() and curr_num in num_set:
                    return False
                else:
                    num_set.add(curr_num)
        return True

    # board: sudoku board to be checked
    # return: true if all rows are valid, false otherwise
    def isValidRows(self, board: List[List[str]]):
        num_set = set()
        # board row and column count is always 9
        for i in range(9):
            for j in range(9):
                curr_num = board[i][j]
                if curr_num.isnumeric() and curr_num in num_set:
                    return False
                else:
                    num_set.add(curr_num)
            num_set.clear()
        return True

    # board: sudoku board to be checked
    # return: true if all columns are valid, false otherwise
    def isValidColumns(self, board: List[List[str]]):
        num_set = set()
        # board row and column count is always 9
        for i in range(9):
            for j in range(9):
                curr_num = board[j][i]
                if curr_num.isnumeric() and curr_num in num_set:
                    return False
                else:
                    num_set.add(curr_num)
            num_set.clear()
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if !(self.isValidRows(board), self.isValidColumns(board)):
            return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if !(self.isValidSubBox(board, (i, j))):
                    return False
        return True