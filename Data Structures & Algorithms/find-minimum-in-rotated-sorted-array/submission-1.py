class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + (r-l)//2
            print(l,r,mid)

            # inSortedSection = False
            # if mid != 0 and nums[mid-1] < nums[mid]:
            #     l = mid + 1

            # if nums[l] < nums[mid]  and nums[r] > nums[mid]:
            #     return nums[l]

            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1

        return nums[l]
