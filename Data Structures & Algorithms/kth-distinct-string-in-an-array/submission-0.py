class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        my_dict = defaultdict(int)
        for string in arr:
            if string not in my_dict:
                my_dict[string] = 1
            else:
                my_dict[string] += 1
        count = 0
        for key in my_dict:
            if my_dict[key] == 1:
                count += 1
                if count == k:
                    return key
        
        return ""