'''
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
'''

'''
[0: [1,2]
 1: [3]
 2: [3]
 3: []]
 
'''


class Solution:
    '''
    result = [[0, 1, 3], [0, 2, 3]]

    path = [0, 2]

    current = 2
    '''

    def allPathsSourceTarget(self, graph):

        self.result = []
        self.dfs(graph, [], 0)

        return self.result

    def getNeighbors(self, g, c):
        return g[c]

    def isGoal(self, g, current):  # 3
        return current == len(g) - 1  # 3 == 3

    def dfs(self, g, path, current):

        c_path = path[:]  # [0]
        c_path.append(current)

        if self.isGoal(g, current):
            self.result.append(c_path)

        neighbors = self.getNeighbors(g, current)  # [1, 2] | [3]

        for n in neighbors:
            self.dfs(g, c_path, n)


s = Solution()

g = [[1, 2], [3], [3], []]
print(s.allPathsSourceTarget(g))
