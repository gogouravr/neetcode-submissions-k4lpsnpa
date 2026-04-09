class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []

        for s in strs:
            # arr = [0 for x in range(26)]
            arr = [0]*26

            for c in s:
                arr[ord(c)-ord('a')] += 1
            
            k = tuple(arr)

            d[tuple(arr)] = d.get(tuple(arr),[])
            d[k].append(s)

        res = [v for k,v in d.items()]
        
        return res

            
        