class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        length = len(words)
        result = []
        for i in range(length):
            for j in range(i + 1, length):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result