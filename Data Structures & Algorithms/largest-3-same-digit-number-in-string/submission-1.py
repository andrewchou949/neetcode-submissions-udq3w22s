class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # current = num[0]
        # so_far = num[0]
        # my_list = set()
        # for i in range(1, len(num)):
        #     # substring starts
        #     if num[i] == current:
        #         so_far += num[i]
        #         if len(so_far) == 3:
        #             my_list.add(int(so_far))
        #     # break
        #     else:
        #         current = num[i]
        #         so_far = num[i]
        # if not my_list:
        #     return ""
        # if max(my_list) == 0:
        #     return "000"
        # return str(max(my_list)) if my_list else ""

        # sliding window approach
        best = ""
        for i in range(len(num) - 2):
            chunk = num[i:i+3]
            if chunk[0] == chunk[1] == chunk[2]:
                if chunk > best:
                    best = chunk
        return best

