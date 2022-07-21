class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        res = 0

        left, right = 0, len(height) - 1
        l, r = height[left], height[right]

        while left < right:
            if l < r:
                left += 1
                l = max(l, height[left])
                res += l - height[left]
            else:
                right -= 1
                r = max(r, height[right])
                res += r - height[right]

        return res
