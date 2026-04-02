class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for item in strs:
            current = sum(ord(x) for x in item)
            if current in my_dict:
                my_dict[current].append(item)
            else:
                my_dict[current] = [item]
        result = []
        for k, v in my_dict.items():
            result.append(v)
        return result