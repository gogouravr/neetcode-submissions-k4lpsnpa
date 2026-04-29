class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m + 1] < nums[m]:
                l = m
                break

            if nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        a,b = 0, l

        while a <= b:
            m = a + (b-a)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                a = m + 1
            else:
                b = m - 1

        a,b = l+1, len(nums) - 1

        while a <= b:
            m = a + (b-a)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                a = m + 1
            else:
                b = m - 1

        return -1

        


