class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        processes = {}
        for c in tasks:
            processes[c] = [processes.get(c,[0])[0] + 1,None]

        def isCompleted():
            for c,l in processes.values():
                if c > 0:
                    return False
            return True

        t = 1
        res = []

        while not isCompleted():
            # print(processes,t)

            keys = list(processes.keys())
            keys.sort(key=lambda x: processes[x][0], reverse=True)

            gotOne = None

            for c in keys:
                if processes[c][0] > 0 and (processes[c][1] is None or processes[c][1] < t - n):
                    # print(c)
                    gotOne = c
                    processes[c][0] -= 1
                    processes[c][1] = t
                    break
            t = t + 1

            # print(processes,t)
            res.append(gotOne)
        # print(res)
        

        return t - 1 

        


        