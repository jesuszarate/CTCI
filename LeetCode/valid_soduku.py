'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

'''


class Solution:
    def isValidSudoku(self, board):

        grid = board

        def checkRows(grid):

            for row in range(len(grid)):
                s = set()
                for col in range(len(grid[0])):
                    val = grid[row][col]
                    if val in s:
                        return False
                    if val != ".":
                        s.add(val)
            return True

        def checkCols(grid):

            for col in range(len(grid[0])):
                s = set()
                for row in range(len(grid)):
                    val = grid[row][col]
                    if val in s:
                        return False
                    if val != ".":
                        s.add(val)
            return True

        def checkSquares(grid):

            t = []
            for r in range(len(grid) // 3):
                t.append([])
                for c in range(len(grid[0]) // 3):
                    t[r].append(set())

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    rv = r // 3
                    cv = c // 3

                    if grid[r][c] in t[rv][cv]:
                        return False

                    if grid[r][c] != ".":
                        t[rv][cv].add(grid[r][c])

            return True

        return checkRows(grid) and checkCols(grid) and checkSquares(grid)


grid = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    [".", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

grid = [[".", ".", ".", ".", ".", ".", "5", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["9", "3", ".", ".", "2", ".", "4", ".", "."],
        [".", ".", "7", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "3", "4", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "."],
        [".", ".", ".", ".", ".", "5", "2", ".", "."]]

s = Solution()

# print(s.isValidSudoku(grid))
import math
print(math.floor(0.5))