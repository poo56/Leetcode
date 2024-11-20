#BRUTE Force
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                result = (min(heights[i],heights[j]) * (j-i))
                res = max(result, res)
        return res


#Optimized 2 pointers

left = 0
right = len(heights) - 1
res = 0
while left < right:
    area = min(heights[left], heights[right]) * (right - left)
    res = max(res, area)
    if heights[left] < heights[right]:
        left +=1
    else:
        right -=1
return res