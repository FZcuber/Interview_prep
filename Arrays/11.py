class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        most = min(height[l], height[r]) * (r - l)

        while l < r:
            left, right = height[l], height[r]
            if left < right:
                l += 1
            else:
                r -= 1
            most = max(most, min(height[l], height[r]) * (r - l))

        return most
