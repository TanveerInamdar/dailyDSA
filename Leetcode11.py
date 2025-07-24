class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        high = 0
        water = 0
        while i < j:
            level = min(height[i], height[j])
            water = level * (j - i)
            if water > high:
                high = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return high


