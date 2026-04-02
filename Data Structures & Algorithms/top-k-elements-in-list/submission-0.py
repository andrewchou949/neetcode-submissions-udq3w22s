class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dummy = [[] for i in range(len(nums) + 1)]
        my_dict = defaultdict(int) # store the count of each element
        for item in nums:
            my_dict[item] += 1
        # loop through each pair of k and v
        for n, v in my_dict.items():
            # v is the count, n is the item
            dummy[v].append(n)
        result = []
        # loop from the back for the biggest count and moving down
        for i in range(len(dummy) - 1, 0, -1):
            for n in dummy[i]:
                result.append(n)
                if len(result) == k:
                    return result