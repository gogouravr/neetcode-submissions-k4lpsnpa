class Solution:
    def climbStairs(self, n: int) -> int:
        slow = 1
        fast = 2
        if n ==1 :
            return 1
        for i in range(2,n):
            ans = slow + fast
            slow = fast
            fast = ans

        return fast