class Solution:
    def isValid(self, s: str) -> bool:
        # We're going to iterate through a string.
        # Let's define a stack for storing open brackets
        stack = []
        # and also define a table of brackets using a hashmap.
        table = {")": "(", "]": "[", "}": "{"}

        # iterate through the input `s`
        for _ in s:
            # catch open brackets and put them in the stack
            if _ in "([{":
                stack.append(_)

            # if _ is a closing bracket, check the top
            # of the stack
            if _ in ")]}":
                # no open brackets
                if stack == []:
                    return False
                # brackets don't match
                if table[_] != stack[-1]:
                    return False
                # matching brackets
                if table[_] == stack[-1]:
                    stack.pop()

        # a valid parenthesis should leave the stack empty
        if stack != []:
            return False

        # GG.
        return True
