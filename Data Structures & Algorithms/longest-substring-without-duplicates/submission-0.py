class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        my_set = set()
        longest = 0
        while right < len(s):
            if s[right] in my_set:
                while s[right] in my_set:
                    my_set.remove(s[left])
                    left += 1
            my_set.add(s[right])
            right += 1
            longest = max(longest, len(my_set))
        return longest
                    

