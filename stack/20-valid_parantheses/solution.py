class Solution:
    # Solution explaination:
    # Iterate through all of the characters
    # If we encounter an opening bracket, push the closing bracket on the stack
    # If we encounter a closing bracket: and the stack is now empty,
    # then we know that we have not had a opening bracket for it. - return false
    # If the closing bracket is not corresponding, return false
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            # If opening bracket
            if c in brackets.keys():
                stack.append(brackets[c])

            # Then we know it is a closing bracket:
            elif not stack or stack.pop() != c:
                return False
        return not stack
