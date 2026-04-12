class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        l = 1
        r = m
        res = 0

        def calHours(mid):
            hours = 0 
            for j in range(len(piles)):
                hours += math.ceil(piles[j]/mid)
            return hours

        while l <= r:
            mid = l + (r-l)//2
            hours = calHours(mid)
            print(l,r,mid,hours)
            if hours > h:
                l = mid + 1
            else:
                res = mid 
                r = mid - 1

        return res  

