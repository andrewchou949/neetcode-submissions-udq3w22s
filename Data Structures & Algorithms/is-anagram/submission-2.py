class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return false immediately when len is no equivalent
        my_dict1 = defaultdict(int)
        my_dict2 = defaultdict(int)
        for char in s:
            my_dict1[char] += 1
        for char in t:
            my_dict2[char] += 1
        return sorted(my_dict1.items(), key = lambda x:x[0]) == sorted(my_dict2.items(), key = lambda x:x[0])
        