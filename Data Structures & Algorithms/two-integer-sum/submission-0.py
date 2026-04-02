class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in my_dict:
                return [my_dict[missing], i]
            my_dict[nums[i]] = i
        return [] # default not found