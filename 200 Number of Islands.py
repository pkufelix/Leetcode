"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    """
    DFS method, find a new '1', change all adjacent '1' to '0' and add 1 to count
    """
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid,i,j)
                count += 1
    return count
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] != '1':
            return
        grid[i][j]='-1'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
    """
    BFS method, find a new '1', add one to count and search all the '1' belongs to same island and change it to '-1'
    """
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] == '-1'
                    que = []
                    que.append([i,j])
                    while que:
                        [row, col] = que.pop(0)
                        if row >= 1 and grid[row-1][col] == '1':
                            que.append([row-1,col])
                            grid[row-1][col] = '-1'
                        if row <= m-2 and grid[row+1][col] == '1':
                            que.append([row+1,col])
                            grid[row+1][col] = '-1'
                        if col >= 1 and grid[row][col-1] == '1':
                            que.append([row,col-1])
                            grid[row][col-1] = '-1'
                        if col <= n-2 and grid[row][col+1] == '1':
                            que.append([row,col+1])
                            grid[row][col+1] = '-1'
        return count