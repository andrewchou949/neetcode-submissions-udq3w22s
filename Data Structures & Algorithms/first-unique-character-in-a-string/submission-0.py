class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_count = Counter(s)
        for i, char in enumerate(s):
            if my_count[char] == 1:
                return i
        return -1