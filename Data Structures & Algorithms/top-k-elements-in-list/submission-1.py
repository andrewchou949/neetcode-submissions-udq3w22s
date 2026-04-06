import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        my_freq = Counter(nums)
        for key, val in my_freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [key for val, key in heap]