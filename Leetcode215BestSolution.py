class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap1 = []

        for i in range(len(nums)):
            heapq.heappush(heap1, nums[i])
            if len(heap1) > k:
                heapq.heappop(heap1)
        return heap1[0]
