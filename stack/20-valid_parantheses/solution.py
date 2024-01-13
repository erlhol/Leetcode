class Solution:
    # Solution explaination:
    # Iterate through all of the characters
    # If we encounter an opening bracket, push it to the stack
    # If we encounter a closing bracket before any opening bracket, return False
    # If we encounter a corresponding opening bracket to the closing bracket, then we pop from the stack
    # If there are any elements left on the stack, that means that we have not found a closing bracket for it
    def isValid(self, s: str) -> bool:
        opening_brackets = []
        brackets = {"(":")","{":"}","[":"]"}
        for c in s:
            # If opening bracket
            if c in brackets.keys():
                opening_brackets.append(c)
                
            # If closing bracket
            elif c in brackets.values():
                if not opening_brackets:
                    return False
                opening = opening_brackets[-1]
                if brackets[opening] == c:
                    opening_brackets.pop()
                else:
                    return False              
        return not opening_brackets
        