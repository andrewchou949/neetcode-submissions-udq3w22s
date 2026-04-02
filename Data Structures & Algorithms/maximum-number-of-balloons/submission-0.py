class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        my_dict = defaultdict(int)
        for char in text:
            if char in target:
                my_dict[char] += 1
        return min(
            my_dict['b'],
            my_dict['a'],
            my_dict['n'],
            my_dict['l'] // 2,
            my_dict['o'] // 2
        )