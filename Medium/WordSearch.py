# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    # Output: true
# Example 2:
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    # Output: true
# Example 3:
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    # Output: false

# Constraints:
    # m == board.length
    # n = board[i].length
    # 1 <= m, n <= 6
    # 1 <= word.length <= 15
    # board and word consists of only lowercase and uppercase English letters.

from typing import List
class Solution:
    
    # returns list of all adjacent cells of given index board[i][j]
    def getAdjacentCells(self, board, i, j):
        result = []
        # above
        if i > 0:
            result.append([board[i-1][j], i-1, j])
        # below
        if i + 1 < len(board):
            result.append([board[i+1][j], i+1, j])
        # right
        if j > 0:
            result.append([board[i][j-1], i, j-1])
        # left
        if j < len(board[0]) - 1:
            result.append([board[i][j+1], i, j+1])
        return result

    # backtrack function to form word by traversing board
    # used = all indexes that are in use
    # curr = current string being built
    # i, j = index of last char added to curr
    def backtracking(self, board, word, used, curr, i, j):
        # if the current string is equal to word then found word
        # return True
        if curr == word:
            return True

        # get all adjacent values of current char board[i][j]
        adjacents = self.getAdjacentCells(board, i, j)
        for val in adjacents:
            c = val[0]
            i_0 = val[1]
            j_0 = val[2]

            # if the char has not been used in curr
            if ([i_0, j_0] not in used):
                # continue if the char is the next letter in the word sequence
                if c == word[len(curr)]:
                    curr += c
                    used_copy = used.copy()
                    used_copy.append([i_0, j_0])
                    if self.backtracking(board, word, used_copy, curr, i_0, j_0):
                        return True
                    # since path was incorrect remove added char
                    curr = curr[:-1]
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        # store all indexes that contains first character of word
        # (starting point of searching the word)
        firstChar = []
        w = word

        # search for the first character of word
        for i in range(len(board)):
            for j in range(len(board[0])):
                # keep track of whether all letters in the word appears
                # in the board
                if board[i][j] in w:
                    w = w.replace(board[i][j], '', 1)
                if board[i][j] == word[0]:
                    firstChar.append([i, j])
        # if the board doesn't have all the letters to make the word
        # then return False
        if len(w) != 0:
            return False

        s = word[0] + ""
        used = []
        # loop through every index that contains the first char of word
        for [i, j] in firstChar:
            used.append([i,j])
            if self.backtracking(board, word, used, s, i, j):
                return True
            used.pop()
        return False