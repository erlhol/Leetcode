from heapq import heappush, heappop, heapify


class Solution:
    # Solution explaination:
    # I convert all the numbers to negative numbers to create the max-heap.
    # Then basically just simulates the process.

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [stone * -1 for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            y = heappop(heap) * -1
            x = heappop(heap) * -1
            if x == y:
                continue
            else:
                heappush(heap, (y - x) * -1)

        return heap[0] * -1 if heap else 0
