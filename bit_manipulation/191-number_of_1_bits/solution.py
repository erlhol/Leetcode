class Solution:
    # Solution explaination:
    # A straight forward, convert from decimal to binary string.
    # Then just count
    def hammingWeight(self, n: int) -> int:
        num = "{:032b}".format(n)
        count = 0
        for i in num:
            if i == "1":
                count += 1
        return count
