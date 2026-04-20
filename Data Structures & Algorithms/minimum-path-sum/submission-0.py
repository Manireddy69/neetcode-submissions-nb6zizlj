class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = [[0]*n for _ in range(m)]
        d[0][0] = grid[0][0]
        for i in range(1, m):
            d[i][0] = grid[i][0] + d[i-1][0]
        for j in range(1, n):
            d[0][j] = grid[0][j] + d[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = grid[i][j] + min(d[i-1][j], d[i][j-1])
        return d[m-1][n-1]