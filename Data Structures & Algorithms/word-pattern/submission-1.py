class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_s = s.split()
        if len(pattern) != len(my_s):
            return False
        p_s = {}
        s_p = {}
        for p, ss in zip(pattern, my_s):
            if p in p_s and p_s[p] != ss:
                return False
            if ss in s_p and s_p[ss] != p:
                return False
            p_s[p] = ss
            s_p[ss] = p
        return True