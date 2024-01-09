class Solution:
    # Solution approach:
    # Keep track of all the numbers: (I call it values)
    # Check if there is a value previously found that mathes with the current value (number)
    # Return the indices immediately if found, else keep going

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        for i in range(1, len(nums)):
            previous_value = nums[i - 1]
            values[previous_value] = i - 1

            current_value = nums[i]
            to_reach = target - current_value
            if to_reach in values:
                return [values[to_reach], i]
