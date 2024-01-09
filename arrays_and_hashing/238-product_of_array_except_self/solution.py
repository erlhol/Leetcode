from collections import deque


class Solution:
    # Solution approach:
    # Create a prefix and postfix list
    # Now multiply in the end with the new list.

    # Time complexity: O(n)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)
        answer = []
        # Fill the prefix list
        prev = 1
        for i in range(len(nums)):
            prev = nums[i] * prev
            prefix[i + 1] = prev

        # Fill the postfix list
        prev = 1
        for i in range(len(nums) - 1, -1, -1):
            prev = nums[i] * prev
            postfix[i] = prev

        for i in range(len(prefix) - 1):
            answer.append(prefix[i] * postfix[i + 1])

        return answer
