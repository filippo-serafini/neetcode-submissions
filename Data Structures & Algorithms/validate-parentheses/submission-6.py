class Solution:
    def isValid(self, s: str) -> bool:
        # We use a stack to keep track of the parentheses
        # Simply, if a bracket is the closing one, then the top of the stack must be the same type opened.

        # Empty stack (list)
        stack = []

        for brack in s:
            if brack == ")" and len(stack) > 0:
                # Check if the top of the stack is "("
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif brack == "]" and len(stack) > 0:
                # Check if the top of the stack is "["
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif brack == "}" and len(stack) > 0:
                # Check if the top of the stack is "{"
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
    
        if len(stack) == 0:
            return True

        return False