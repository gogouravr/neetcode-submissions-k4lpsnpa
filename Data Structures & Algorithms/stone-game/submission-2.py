class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def rec(i=0,j=len(piles)-1) -> int:
            # print(i,j,alice,bob)

            k = (i,j)
            if k in dp:
                return dp[k]

            if i > j:
                return 0

            l = rec(i+1,j-1) + piles[i]
            r= rec(i+1,j-1) + piles[j]
            
            dp[k] = max(l,r)
            return dp[k]

        aliceMaxPossible = rec() 
        return aliceMaxPossible > sum(piles) - aliceMaxPossible
        