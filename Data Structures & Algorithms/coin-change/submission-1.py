class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def minNumCoins(left=amount):
            if left in dp:
                return dp[left]

            if left == 0:
                return 0

            res = 10**10
            for coin in coins:
                if left - coin >= 0:
                    res = min(res, 1 + minNumCoins(left-coin))

            dp[left] = res
            return res

        ans = minNumCoins()
        return ans if ans != 10**10 else -1