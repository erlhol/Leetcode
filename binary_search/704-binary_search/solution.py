class Solution:
    # A simple binary search without using libraries
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            i = (low + high) // 2
            if nums[i] < target:
                low += 1
            elif nums[i] > target:
                high -= 1
            else:
                return i
        return -1