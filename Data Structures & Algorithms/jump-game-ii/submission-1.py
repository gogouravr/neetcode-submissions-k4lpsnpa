class Solution:
    def jump(self, nums: List[int]) -> int:
        
        res = 10**10

        def rec(i=0):
            if i >= len(nums) - 1:
                return 0

            min_jumps = 10**10
            for j in range(1,nums[i]+1):
                min_jumps = min(min_jumps, 1 + rec(j))

            return min_jumps


        # return rec()



        dp = [10**10]*len(nums)
        dp[0] = 0
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], 1 + dp[j])
        print(dp)
        return dp[len(nums)-1]
