class Solution:

    def encode(self, strs: List[str]) -> str:
        newS = ""
        for s in strs:
            newS += str(len(s))
            newS += '#'
            newS += s

        return newS

    def decode(self, s: str) -> List[str]:
        i =0
        res = []
        while i < len(s):
            n = ""

            while s[i] >= '0' and s[i] <= '9':
                n += s[i]
                i += 1
            
            l = int(n)
            j = i + 1
            v = ""
            while j < i+l+1:
                v += s[j]
                j += 1

            res.append(v)
            i = j

        return res



