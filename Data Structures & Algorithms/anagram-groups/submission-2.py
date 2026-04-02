class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            # 1. Create the fixed-size frequency array (26 letters)
            count = [0] * 26
            for char in s:
                # Map 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
                index = ord(char) - ord('a')
                count[index] += 1
            
            # 2. Convert list to tuple to use as a dictionary key
            key = tuple(count)
            
            # 3. Group the original string
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
            
        return list(groups.values())