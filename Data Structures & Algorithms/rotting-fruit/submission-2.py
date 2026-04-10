class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])
        cells = [[0,1],[0,-1], [1,0],[-1,0]]

        def isValid(i,j):
            return not (i < 0 or i >= n or j < 0 or j >= m)

        vis = []

        for i in range(n):
            vis.append([])
            for j in range(m):
                vis[i].append(0)

        
        q = deque()


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])

        
        res = 0
        while len(q) != 0:

            l = len(q)

            for i in range(l):
                u,v = q.popleft()
                grid[u][v] = 2
                
                

                for i,j in cells:
                    if isValid(u+i,v+j) and vis[u+i][v+j] == 0 and grid[u+i][v+j] == 1:
                        q.append([u+i,v+j])
                        vis[u+i][v+j] = 1
            if len(q) != 0:
                res += 1 

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1


        return res



            
            


        