class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = 0
        s = 0
        firstPass = True

        while f != s or firstPass:
            f = nums[nums[f]]
            s = nums[s]
            firstPass = False
        print(f,s)
        s = 0

        while f != s:
            f = nums[f]
            s = nums[s]

        return f

        
        