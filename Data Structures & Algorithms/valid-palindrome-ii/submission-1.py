class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True # palin on its own (prevent unnecessary loop)
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return self.palin(s, left + 1, right) or self.palin(s, left, right - 1)
            left += 1
            right -= 1
        return False

    def palin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
