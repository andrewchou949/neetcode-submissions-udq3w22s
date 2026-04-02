class Solution:
    def minOperations(self, logs: List[str]) -> int:
        my_stack = []
        current = ""
        for log in logs:
            if log == "../":
                if my_stack:
                    current = my_stack.pop()
            elif log == "./":
                continue
            else:
                my_stack.append(log)
                current = log
        print(my_stack)
        return len(my_stack)
