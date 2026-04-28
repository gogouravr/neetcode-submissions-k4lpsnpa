class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def isWordPossible(i=0):
            if i in dp:
                return dp[i]

            if i == len(s):
                return True

            res = False

            for word in wordDict:
                length_left = len(s) - i
                if len(word) <= length_left and word == s[i:i+len(word)]:
                    res = res or isWordPossible(i+len(word))
            dp[i] = res
            return res

        # return isWordPossible()

        dp2 = [False] * (len(s))

        for i in range(len(s)):
            for j in range(i-1,-1,-1):
                print( s[j+1:i+1])
                if dp2[j] == True and s[j+1:i+1] in wordDict:
                    dp2[i] = True
                    break
            dp2[i] = dp2[i] or s[:i+1] in wordDict

        print(dp2)
        return dp2[-1]




        
        