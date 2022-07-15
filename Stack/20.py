class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        Map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for i in range(len(s)):
            if s[i] in Map:
                stack.append(s[i])
            elif not stack or Map[stack[-1]] != s[i]:
                return False
            else:
                stack.pop()

        return stack == []


f = Solution()
print(f.isValid("(("))
