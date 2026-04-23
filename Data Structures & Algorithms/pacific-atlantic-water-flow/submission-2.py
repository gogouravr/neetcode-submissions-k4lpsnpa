class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        n,m = len(h),len(h[0])
        isValid = lambda i,j: i >= 0 and j >=0 and i < n and j < m
        p = lambda i,j: i == 0 or j == 0
        a = lambda i,j: j == m -1 or i == n -1

        memo = {}

        def dfs(i,j,vis = set()):
            print(i,j)
            if (i,j) in memo:
                return memo[(i,j)]

            if p(i,j) and a(i,j):
                memo[(i,j)] = (True,True)
                return (True,True)

            res = [p(i,j),a(i,j)]

            vis.add((i,j))

            for u,v in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                ix , jx = u,v
                if isValid(ix,jx) and (ix,jx) not in vis and h[ix][jx] <= h[i][j]:
                    tRes = dfs(ix,jx,vis)
                    res[0] = res[0] or tRes[0]
                    res[1] = res[1] or tRes[1]


                
            for u,v in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                ix , jx = u,v
                if isValid(ix,jx) and (ix,jx) not in vis and h[ix][jx] == h[i][j]:
                    memo[(ix,jx)] = [memo[(ix,jx)][0] or res[0] , memo[(ix,jx)][1] or res[1]]



            vis.remove((i,j))
            memo[(i,j)] = res
            # print(i,j," ",memo[(i,j)])
            return res

        ans = []

        for i in range(n):
            for j in range(m):
                print(h[i][j],end=" ")
            print()

        for i in range(n):
            for j in range(m):
                if (i,j) not in memo:
                    dfs(i,j)

        # print(memo)


        # for i in range(n):
        #     for j in range(m):
        #         if False not memo[(i,j)]:
        #             for 

        for [k,v] in memo.items():
            if False not in v:
                ans.append(list(k))
        ans.sort()
        return ans

            