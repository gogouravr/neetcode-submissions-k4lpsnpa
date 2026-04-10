class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPal(s):
            i = 0
            j = len(s) - 1

            while i  < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        def isArrPal(arr):
            for s in arr:
                if not isPal(s):
                    return False
            return True

        def choice(i,ans):
            if i == len(s):
                if isArrPal(ans):
                    res.append(ans[:])
                return
            
            lastS = ans[-1] 
            choice(i+1,ans[:-1]+[lastS + s[i]])

            choice(i+1, ans + [s[i]])

        choice(1,[s[0]])

        return res

        