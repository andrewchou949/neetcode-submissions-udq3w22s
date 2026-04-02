class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for code in details:
            age = int(code[11:13])
            print(age)
            if age > 60:
                count += 1
        return count
        