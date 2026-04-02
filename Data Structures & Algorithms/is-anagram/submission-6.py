class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_s, my_t = Counter(s), Counter(t)
        for k in my_s:
            if k not in my_t or my_s[k] != my_t[k]:
                return False
        return True