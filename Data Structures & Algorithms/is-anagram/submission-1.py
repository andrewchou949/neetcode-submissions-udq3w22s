class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return false immediately when len is no equivalent
        if len(s) != len(t):
            return False
        my_s = defaultdict(int)
        my_t = defaultdict(int)
        for i in range(len(s)):
            my_s[s[i]] += 1
            my_t[t[i]] += 1
        for item in my_s.keys():
            if my_s[item] != my_t[item]:
                return False
        return True