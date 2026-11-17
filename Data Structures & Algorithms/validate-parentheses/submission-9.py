class Solution:
    def isValid(self, s: str) -> bool:
        # We use a stack to keep track of the parentheses
        # Simply, if a bracket is the closing one, then the top of the stack must be the same type opened.

        # Empty stack (list)
        stack = []
        # Create an Hashet for O(1) lookups containing:
        #       Key: close bracket
        #       Value: open bracket
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for brack in s:
            # Check if the character is a close bracket
            if brack in closeToOpen:
                if stack and stack[-1] == closeToOpen[brack]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
    
        return True if not stack else False