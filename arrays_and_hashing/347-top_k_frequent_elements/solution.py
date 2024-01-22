class Solution:
    # TODO: Add explaination

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        return [
            k for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])
        ][0:k]
