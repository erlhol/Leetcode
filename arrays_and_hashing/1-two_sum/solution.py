class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        i = 1
        while i < len(nums):
            n = nums[i - 1]
            numbers[n] = i - 1

            p = nums[i]
            to_reach = target - p
            if to_reach in numbers:
                return [numbers[to_reach], i]

            i += 1
