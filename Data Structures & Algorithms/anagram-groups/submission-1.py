class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for item in strs:
            current = tuple(sorted(item))
            if current in my_dict:
                my_dict[current].append(item)
            else:
                my_dict[current] = [item]
        result = list(sorted(my_dict.values(), key=lambda x: len(x)))
        return result