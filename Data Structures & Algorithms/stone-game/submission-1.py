class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def rec(i=0,j=len(piles)-1,alice=0, bob=0):
            # print(i,j,alice,bob)
            k = (i,j,alice,bob)
            if k in dp:
                return dp[k]

            if i > j:
                return alice > bob
            
            dp[k] = rec(i+1,j-1,alice+piles[i],bob+piles[j]) or  rec(i+1,j-1,alice+piles[j],bob+piles[i])
            return dp[k]

        return rec()
        