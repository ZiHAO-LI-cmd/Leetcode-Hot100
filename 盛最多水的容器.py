class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针
        left = 0
        right = len(height) - 1
        maxValue = 0
        while left < right:
            curValue = min(height[left], height[right]) * (right - left)
            maxValue = max(maxValue, curValue)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxValue
