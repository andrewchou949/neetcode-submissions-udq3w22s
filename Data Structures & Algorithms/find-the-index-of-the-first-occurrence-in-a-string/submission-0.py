class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle) or not len(haystack) or not len(needle):
            return -1
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            current = haystack[i:i+length]
            if current == needle:
                return i
        return -1