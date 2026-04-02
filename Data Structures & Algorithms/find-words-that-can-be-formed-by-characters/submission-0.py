class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        my_chars = Counter(chars)
        total = 0
        for word in words:
            valid = True
            eac = Counter(word)

            for k in eac:
                if eac[k] > my_chars[k]:
                    valid = False
                    break
            
            if valid:
                total += len(word)
        return total