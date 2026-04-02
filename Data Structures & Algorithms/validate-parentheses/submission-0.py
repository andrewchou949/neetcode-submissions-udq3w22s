class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        my_stack = []
        for char in s:
            if char in my_dict.keys():
                my_stack.append(char)
            else:
                if not my_stack:
                    return False
                top = my_stack.pop()
                if char != my_dict[top]:
                    return False

        return len(my_stack) == 0