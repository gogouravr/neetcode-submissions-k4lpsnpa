class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
         
        def isValid(i,j):
            return i >= 0 and i< n and j >= 0 and j < m

        vis = set()

        def dfs(i,j):
            # print(i,j)
            vis.add((i,j))

            for u,v in [[0,1],[0,-1],[1,0],[-1,0]]:
                r = u + i
                c = v + j

                if (r,c) not in vis and isValid(r,c) and grid[r][c] == '1':
                    dfs(r,c)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in vis:
                    res += 1
                    dfs(i,j)

        return res





        