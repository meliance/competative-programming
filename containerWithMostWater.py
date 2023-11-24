class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j =0, len(height) - 1
        maxArea = -maxsize
        while i < j:
            shorter_line = min(height[i], height[j])
            maxArea = max(maxArea, shorter_line * (j - i)) 
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea