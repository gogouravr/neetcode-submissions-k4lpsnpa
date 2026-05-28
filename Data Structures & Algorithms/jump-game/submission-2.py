class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def recursion(i: int):
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return False

            if i == len(nums)-1:
                return True

            res = False

            for j in range(1,nums[i]+1):
                res = res or recursion(i+j)

            dp[i] = res
            return res

        # return recursion(0)

        max_jump_possible_upto = nums[0]

        for i in range(1,len(nums)):
            if max_jump_possible_upto < i:
                return False
            max_jump_possible_upto = max(max_jump_possible_upto, i + nums[i])
            
        return True

        