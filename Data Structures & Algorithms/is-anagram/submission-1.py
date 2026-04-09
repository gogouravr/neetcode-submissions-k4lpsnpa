class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        for c in s:
            freqS[c] = freqS.get(c,0) + 1

        for c in t:
            freqT[c] = freqT.get(c,0) + 1

        if len(freqT) != len(freqS):
            return False

        for k,v in freqS.items():
            if k not in freqT or v != freqT[k]:
                return False

        return True        