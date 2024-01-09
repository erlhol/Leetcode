class Solution:
    # Solution approach:
    # 1. Iterate over each charachter and create a string of it, only adding alphanumeric or numeric
    # 2. Then use a two pointer approach to see if each of ends of the strings are equal.
    # If they are not equal, it is not a palindrome.

    # Time complexity: O(n)

    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        text = ""
        for c in t:
            if c.isalpha() or c.isnumeric():
                text += c
        low = 0
        high = len(text) - 1
        while low < high:
            if text[low] != text[high]:
                return False
            low += 1
            high -= 1
        return True
