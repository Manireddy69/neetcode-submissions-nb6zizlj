class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ## you will get the formula
        ## 4 * cells - 2 * edges
        m = len(grid)
        n = len(grid[0])
        cells = 0
        edges = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    cells += 1
                    if  r + 1 < m and grid[r+1][c] == 1:
                        edges += 1
                    if c+ 1 < n and grid[r][c+1] == 1:
                        edges += 1
        return 4 * cells - 2 * edges