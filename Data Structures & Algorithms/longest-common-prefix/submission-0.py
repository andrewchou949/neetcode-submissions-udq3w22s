class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_length = float('inf')
        for char in strs:
            min_length = min(min_length, len(char))
        res = ""
        for i in range(min_length):
            for char in strs:
                if char[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        


