'''
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.


You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input:
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6


Example 2:

Input:
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1


Example 3:

Input:
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.


Hint: size of the given matrix will not exceed 50x50.
'''


class Node:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbors = []


class Solution:
    def cutOffTree(self, forest) -> int:
        target = Node(len(forest) - 1, len(forest[0]) - 1)
        visited = [[False for _ in range(len(forest[0]))] for _ in range(len(forest))]
        total_steps = self.search(forest, visited, Node(0, 0), target)

        if not self.isAllCut(forest):
            return -1

        return total_steps

    def isAllCut(self, forest):

        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] > 1:
                    return False
        return True


    def search(self, grid, visited, root, target):
        q = [root]

        steps = -1
        while q:
            current = q[0]

            del q[0]
            steps += 1
            self.cutTheTree(grid, current)
            visited[current.row][current.col] = True

            neighbors = self.getNeighbors(grid, visited, current)
            for n in neighbors:
                q.append(n)

        return steps

    def cutTheTree(self, forest, tree):
        forest[tree.row][tree.col] = 1

    def getNeighbors(self, grid, visited, node):
        '''
        Only return neighbors that are not 0.
        '''
        r = node.row
        c = node.col
        possible_neighbors = [Node(r - 1, c), Node(r + 1, c), Node(r, c - 1), Node(r, c + 1)]

        neighbors = []
        for n in possible_neighbors:

            if n.row > -1 and n.col > -1 and n.row < len(grid) and n.col < len(grid[0]):
                if grid[n.row][n.col] > 1 and not visited[n.row][n.col]:
                    neighbors.append(n)

        return neighbors


s = Solution()

forest = [
    [1, 2, 3],
    [1, 0, 4],
    [7, 6, 5]
]

# forest = [
#     [1, 2, 3],
#     [0, 0, 0],
#     [7, 6, 5]
# ]

forest = [[54581641,64080174,24346381,69107959],
          [86374198,61363882,68783324,79706116],
          [668150,92178815,89819108,94701471],
          [83920491,22724204,46281641,47531096],
          [89078499,18904913,25462145,60813308]]

print(s.cutOffTree(forest))
