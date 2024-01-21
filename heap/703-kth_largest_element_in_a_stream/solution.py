from heapq import heappush, heappop


class KthLargest:
    # Solution explaination

    # Only add to the heap larger element than the current smallest
    # This gurarantees that the smallest element in this heap is the kth largest

    def __init__(self, k: int, nums: List[int]):
        self.numbers = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.numbers) < self.k:
            heappush(self.numbers, val)
            return self.numbers[0]

        if val > self.numbers[0]:
            heappop(self.numbers)
            heappush(self.numbers, val)
        return self.numbers[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
