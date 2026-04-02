class Solution:
    def maxScore(self, s: str) -> int:
        result = float('-inf')
        for i in range(len(s)):
            left, right = s[0:i+1], s[i+1:]
            if left and right:
                cal = left.count("0") + right.count("1")
            result = max(result, cal)
            
        return result