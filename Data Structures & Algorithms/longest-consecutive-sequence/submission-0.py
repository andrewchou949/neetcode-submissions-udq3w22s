class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for num in nums:
            # find the first valid number by checking if previoous number of current exist?
            if num - 1 not in my_set:
                current = 1
                while num + 1 in my_set:
                    current += 1
                    num += 1
                longest = max(current, longest)
        return longest
