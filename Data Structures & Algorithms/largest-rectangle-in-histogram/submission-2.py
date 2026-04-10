class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        minStk = []
        maxStk = []
        n = len(heights)
        firstSmallerEleToTheLeft = []
        firstSmallerEleToTheRight = []

        for i in range(len(heights)):
            while len(minStk) > 0 and  heights[minStk[-1]] >= heights[i]:
                minStk.pop()
            if len(minStk) == 0:
                firstSmallerEleToTheLeft.append(-1)
            else:
                firstSmallerEleToTheLeft.append(minStk[-1])

            minStk.append(i)

        for i in range(len(heights)-1,-1,-1):
            while len(maxStk) > 0 and heights[maxStk[-1]] >= heights[i]:
                maxStk.pop()

            if len(maxStk) == 0:
                firstSmallerEleToTheRight.append(n)
            else:
                firstSmallerEleToTheRight.append(maxStk[-1])

            maxStk.append(i)

        

        
        res = 0

        firstSmallerEleToTheRight.reverse()


        for i in range(len(heights)):
            res = max(res, heights[i]*(firstSmallerEleToTheRight[i]-firstSmallerEleToTheLeft[i]-1))

        return res

            
