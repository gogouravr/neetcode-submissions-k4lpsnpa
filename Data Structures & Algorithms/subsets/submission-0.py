class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(i,arr):
            if i == len(nums):
                res.append(arr)
                return
            
            rec(i+1,[*arr, nums[i]])
            rec(i+1,arr)

        rec(0,[])

        return res
            
        