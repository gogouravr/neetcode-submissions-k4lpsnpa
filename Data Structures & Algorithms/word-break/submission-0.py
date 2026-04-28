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

        return isWordPossible()


        
        