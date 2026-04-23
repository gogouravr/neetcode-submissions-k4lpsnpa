class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g = {}

        for i in range(1,len(words)):

            # for i in range(1,len(word)):
            #     if word[i-1] not in g:
            #         g[word[i-1]] = []
            #     if word[i] not in g:
            #         g[word[i]] = []
            #     if word[i] != word[i-1] and word[i] not in g[word[i-1]]:
            #         g[word[i-1]].append(word[i])

            j = 0
            while j < min(len(words[i]),len(words[i-1])):
                if words[i][j] != words[i-1][j]:
                    break
                j += 1


            if j ==  min(len(words[i]),len(words[i-1])):
                if len(words[i]) < len(words[i-1]):
                    return ""
                continue

            if words[i-1][j] not in g:
                g[words[i-1][j]] = []

            if words[i][j] not in g[words[i-1][j]]:
                g[words[i-1][j]].append(words[i][j])

        
        for word in words:
            for c in word:
                if c not in g:
                    g[c] = []

        # edges = 0
        # for c in g.keys():
        #     edges += len(g[c])

        # if edges == 0 and len(g.keys()) != 1:
        #     return ""
            


            


        res = ""
        isCycle = False
        print(g)


        def dfs(v, vis= set()):
            print(v,vis)
            nonlocal res
            nonlocal isCycle
            if v in vis:
                isCycle = True
                return

            if v in res:
                return
            
            vis.add(v)
            for c in g[v]:
                dfs(c,vis)

            vis.remove(v)
            print('adding ', v, ' to ' , res)
            res = v + res


        ans = ""

        for k in g.keys():
            print('calling',k)
            dfs(k)

        return "" if isCycle else res




        