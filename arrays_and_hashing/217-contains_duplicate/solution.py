class Solution:
    # Solution approach:
    # Iterate through the numbers and add them to a map.
    # If the number is seen, then return True, else, keep iterating

    # Interesting here is that dictionary is actually faster on this particular
    # input data. Could have used a set here instead, but it is a little bit slower

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for n in nums:
            if n in seen:
                return True
            seen[n] = 1
        return False
