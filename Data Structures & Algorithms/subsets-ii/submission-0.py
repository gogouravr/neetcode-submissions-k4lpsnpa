class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        arr = []
        
        def rec(i):
            res.append(arr[:])
            for j in range(i,len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                arr.append(nums[j])
                rec(j+1)
                arr.pop()

        
        rec(0)
        return res
        