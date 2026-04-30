class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,1

        res = 1
        seen = set()
        seen.add(s[0])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res,r-l+1)
            r += 1

        return res



        