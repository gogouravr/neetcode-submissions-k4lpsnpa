class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = {}

        if len(s3) != len(s1) + len(s2):
            return False

        def rec(i,j):
            print(i,j)
            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(s1) and j == len(s2):
                return True

            idx = i+j

            res = False

            if len(s1) != i and s1[i] == s3[idx]:
                res = res or rec(i+1,j)    
            
            if len(s2) != j and s2[j] == s3[idx]:
                res = res or rec(i,j+1)

            dp[(i,j)] = res
            return res

        return rec(0,0)
        