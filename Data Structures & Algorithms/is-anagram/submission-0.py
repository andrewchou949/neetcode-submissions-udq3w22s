class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return false immediately when len is no equivalent
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)