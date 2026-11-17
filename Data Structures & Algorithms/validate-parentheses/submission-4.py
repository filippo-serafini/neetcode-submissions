class Solution:
    def isValid(self, s: str) -> bool:
        # We use a stack to keep track of the parentheses
        # Simply, if a bracket is the closing one, then the top of the stack must be the same type opened.

        # Empty stack (list)
        stack = []
        opened = 0
        closed = 0

        for brack in s:
            if brack == ")" and len(stack) > 0:
                # Check if the top of the stack is "("
                closed += 1
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif brack == "]" and len(stack) > 0:
                # Check if the top of the stack is "["
                closed += 1
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif brack == "}" and len(stack) > 0:
                # Check if the top of the stack is "{"
                closed += 1
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
                opened += 1
    
        if opened == closed:
            return True
        return False