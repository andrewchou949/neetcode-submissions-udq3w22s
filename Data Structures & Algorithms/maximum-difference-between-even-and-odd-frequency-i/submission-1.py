class Solution:
    def maxDifference(self, s: str) -> int:
        my_dict = Counter(s)
        max_odd, min_even = float('-inf'), float('inf')
        for value in my_dict.values():
            if value % 2 != 0:
                max_odd = max(max_odd, value)
            if value % 2 == 0:
                min_even = min(min_even, value)
        return max_odd - min_even