class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # res = 10**10

        # def rec(i=0):
        #     if i >= len(nums) - 1:
        #         return 0

        #     min_jumps = 10**10
        #     for j in range(1,nums[i]+1):
        #         min_jumps = min(min_jumps, 1 + rec(j))

        #     return min_jumps


        # return rec()



        # dp = [10**10]*len(nums)
        # dp[0] = 0
        # for i in range(1,len(nums)):
        #     for j in range(i-1,-1,-1):
        #         if nums[j] + j >= i:
        #             dp[i] = min(dp[i], 1 + dp[j])
        # print(dp)
        # return dp[len(nums)-1]
        if len(nums) == 1:
            return 0


        max_ach_pos = nums[0]
        curr_max = 0
        res = 1
        i = 1

        for t in range(1,len(nums)):
            print(t,max_ach_pos,curr_max)
            if t > max_ach_pos:
                max_ach_pos = curr_max
                res += 1
            curr_max = max(curr_max,t+nums[t])

        return res



        while i < len(nums):
            print(i)

            j = i 
            curr_max_ach_pos = 0
            while j <= max_ach_pos and j < len(nums) - 1:
                curr_max_ach_pos = max(curr_max_ach_pos, j + nums[j])
            res += 1

            i = max_ach_pos + 1
            max_ach_pos = curr_max_ach_pos

            if curr_max_ach_pos >= len(nums) - 1:
                return res

        return -1




            
