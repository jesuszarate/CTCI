
'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1: 
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.


Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


'''
class Solution:
    
    def orangesRotting(self, grid):

        # Initially add all the rotten oranges to the queue
        q = []
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 2:
                    q.insert(0, (row, col))

        # Do a BFS and each level of BFS is an elabsed minute
        level = 0
        while len(q) > 0:
            
            size = len(q)

            while size > 0:                
                pos = q.pop()

                print("popped: ", pos)
                row = pos[0]
                col = pos[1]

                # Top
                if row > 0:
                    self.visit_and_add(grid, row - 1, col, q)
                    
                # Bottom
                if row < len(grid) - 1:
                    self.visit_and_add(grid, row + 1, col, q)
                    
                # Left
                if col > 0:
                    self.visit_and_add(grid, row, col - 1, q)

                # Right
                if col < len(grid[0]) - 1:
                    self.visit_and_add(grid, row, col + 1, q)                

                size -= 1

            # We only count this as a level if we converted any oranges to BAD
            if len(q) > 0:
                level += 1

        # One last check to make sure there aren't any fresh oranges left
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1


        return level

    def visit_and_add(self, grid, row, col, q):        
        if grid[row][col] == 1:
            grid[row][col] = 2
            q.insert(0, (row, col))
        
        
        
if __name__ == "__main__":

    an = Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    print(an)
