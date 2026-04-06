class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} # {target - num, index of num}
        for i, num in enumerate(nums):
            missing = target - num
            # found
            if missing in my_dict:
                return [my_dict[missing], i]
            my_dict[num] = i 
        return []