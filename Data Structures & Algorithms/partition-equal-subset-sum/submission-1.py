class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s%2 == 1:
            return False

        dp = {}

        def rec(i=0,reqSum=(s//2)):
            if (i,reqSum) in dp:
                return dp[(i,reqSum)]

            if reqSum == 0:
                return True
            if i == len(nums):
                return False

            dp[(i,reqSum)]= rec(i+1,reqSum - nums[i]) or \
            rec(i+1,reqSum)

            return dp[(i,reqSum)]


        return rec()
