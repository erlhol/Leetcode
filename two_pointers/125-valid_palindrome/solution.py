class Solution:
    # Solution approach:
    # Use a two pointer approach to see if each of ends of the strings are equal.
    # Increment the pointers while it is not a number or alphanumeric charachter
    # If they are not equal, it is not a palindrome.

    # Time complexity: O(n)

    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1
        while low < high:
            while low < high and not (s[low].isalpha() or s[low].isnumeric()):
                low += 1
            while low < high and not (s[high].isalpha() or s[high].isnumeric()):
                high -= 1

            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True
