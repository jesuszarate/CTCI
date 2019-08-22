'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''


class Solution:
    def exist(self, board, word):

        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                    visited[r][c] = True
                    if self.exist_rec(board, word, visited, 1, r, c):
                        return True

        return False

    def exist_rec(self, board, word, visited, pos, row, col):

        if pos == len(word):
            return True

        neighbors = self.get_neighbors(board, visited, row, col)

        for n in neighbors:
            if n['val'] == word[pos]:
                visited[n['row']][n['col']] = True
                if self.exist_rec(board, word, visited, pos + 1, n['row'], n['col']):
                    return True
                visited[n['row']][n['col']] = False

        return False

    def get_neighbors(self, board, visited, row, col):

        neighbors = [{'val': None, 'row': row, 'col': col + 1},
                     {'val': None, 'row': row, 'col': col - 1},
                     {'val': None, 'row': row + 1, 'col': col},
                     {'val': None, 'row': row - 1, 'col': col}]

        for n in neighbors:
            if n['row'] >= 0 and n['row'] < len(board) and n['col'] >= 0 and n['col'] < len(board[0]):
                if not visited[n['row']][n['col']]:
                    n['val'] = board[n['row']][n['col']]

        return list(filter(lambda n: n['val'] is not None, neighbors))


s = Solution()

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

print(s.exist(board, "ABCCED") == True)
print(s.exist(board, "SEE") == True)

board = [["C", "A", "A"],
         ["A", "A", "A"],
         ["B", "C", "D"]]

print(s.exist(board, "AAB") == True)

board = [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]]

word = "ABCESEEEFS"

print(s.exist(board, word) == True)
