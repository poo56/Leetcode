class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_area = 0
        left = 0
        right = len(height) - 1
        
        while(left<=right):
            current_area = max(current_area,min(height[left],height[right]) * (right-left))
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return current_area
