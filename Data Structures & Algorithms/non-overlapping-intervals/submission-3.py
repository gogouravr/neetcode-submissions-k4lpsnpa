class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1],-1*x[0]))

        boundary = intervals[0][1]
        ans = 0

        print(intervals)

        for i in range(1,len(intervals)):
            if intervals[i][0] < boundary:
                ans += 1
            else:
                boundary = max(boundary,intervals[i][1])

        return ans
            





        