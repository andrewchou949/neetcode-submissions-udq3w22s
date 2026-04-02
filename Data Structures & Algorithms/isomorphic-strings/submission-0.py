from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for chars, chart in zip(s, t):
            if chars in s_to_t and s_to_t[chars] != chart:
                return False
            if chart in t_to_s and t_to_s[chart] != chars:
                return False
            s_to_t[chars] = chart
            t_to_s[chart] = chars
        
        return True