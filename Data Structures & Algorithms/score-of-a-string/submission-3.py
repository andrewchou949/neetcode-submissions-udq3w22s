class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        if len(s) == 0 or len(s) == 1:
            return 0
        for i in range(1, len(s)):
            score += abs(ord(s[i]) - ord(s[i - 1]))
        return score