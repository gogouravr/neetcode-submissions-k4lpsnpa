class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        safe = {}
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j = i + 1
            k = len(nums)-1
            # print(nums)
            while j < k:
                if nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1


                if j != k and ((nums[i],nums[j],nums[k]) not in safe ) and nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    safe[(nums[i],nums[j],nums[k])] = True
                    # print(i,j,k)

                if nums[i] + nums[j] + nums[k] == 0:
                    j += 1
                    k -= 1

        return res
            

                


