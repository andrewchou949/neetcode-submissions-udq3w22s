class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            n = len(item)
            delimiter = str(n) + "#"
            to_add = delimiter + item
            res += to_add
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # finding the entire length string first
            j = i
            while str(s[j]) != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

