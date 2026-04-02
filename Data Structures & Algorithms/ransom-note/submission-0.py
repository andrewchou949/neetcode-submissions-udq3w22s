class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        maga = Counter(magazine)
        for k, v in ran.items():
            if k not in maga:
                return False
            # k is in already
            if ran[k] > maga[k]:
                return False

        return True