class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # to store number only
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]