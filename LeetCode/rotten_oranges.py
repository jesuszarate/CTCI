class Solution:
    def orangesRotting(self, grid):
        
        self.max_depth = 0
        rotten = self.findRotten(grid)
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        min_minutes = float("inf")
        for rotten_orange in rotten:
            min_minutes = min(self.rotOranges(grid, visited, rotten_orange), min_minutes)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1        
        
        return min_minutes
    
    def rotOranges(self, grid, visited, orange):        
        visited[orange[0]][orange[1]] = True
        grid[orange[0]][orange[1]] = 2
        neighbors = self.getNeighbors(grid, visited, orange)
        
        if not neighbors:
            return 0

        max_depth = 0
        for neighbor in neighbors:
            current_depth = self.rotOranges(grid, visited, neighbor)
            max_depth = max(current_depth, max_depth)            
        return max_depth + 1
            
    
    def getNeighbors(self, grid, visited, orange):
        row = orange[0]
        col = orange[1]
        neighbors = [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]        
        valid_neighbors = []
        for neighbor in neighbors:            
            if neighbor[0] >= 0 and neighbor[0] < len(grid):
                if neighbor[1] >= 0 and neighbor[1] < len(grid[0]):
                    c_orange = grid[neighbor[0]][neighbor[1]]
                    if not visited[neighbor[0]][neighbor[1]] and c_orange == 1:
                        valid_neighbors.append(neighbor)
        return valid_neighbors
                    
    
    def isRotten(self, grid, row, col):
        return grid[row][col] == 2
    
    def findRotten(self, grid):        
        rotten = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):                
                if self.isRotten(grid, row, col):
                    rotten.append((row, col))                    
        return rotten

s = Solution()

grid = [[2,1,1,0],[1,1,0,0],[0,0,0,2],[0,1,1,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[0,2]]

print(s.orangesRotting(grid))