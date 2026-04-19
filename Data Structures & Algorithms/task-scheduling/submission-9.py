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
        while not isCompleted():
            keys = [(c,k) for k, [c,l] in processes.items()]
            heapq._heapify_max(keys)

            while len(keys) > 0 and (processes[keys[0][1]][0] == 0 or  not (processes[keys[0][1]][1] is None or processes[keys[0][1]][1] < t - n)):
                heapq.heappop(keys)

            if len(keys) > 0:
                processes[keys[0][1]][0] -= 1
                processes[keys[0][1]][1] = t

            # for c in keys:
            #     if processes[c][0] > 0 and (processes[c][1] is None or processes[c][1] < t - n):
            #         gotOne = c
            #         processes[c][0] -= 1
            #         processes[c][1] = t
            #         break



            t = t + 1

        

        return t - 1 

        


        