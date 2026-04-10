class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx = {}

        for i in range(len(nums)):
            idx[nums[i]] = True
        
        res = 0
        
        for i in range(len(nums)):
            
            if nums[i] -1 not in idx:
                j = 1
                while nums[i] + j in idx:
                    j += 1
                res = max(res,j) 

        return res
