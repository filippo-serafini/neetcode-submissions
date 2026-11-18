class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Keep a stack for each number, when I meet an operation, pop the head [-1] and the previous one [-2] and save them in append
        stack = []

        ops = {"+", "-", "*", "/"}

        for el in tokens:
            if el not in ops:
                stack.append(int(el))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                if el == "+":
                    stack.append(num_1 + num_2)
                elif el == "-":
                    stack.append(num_1 - num_2)
                elif el == "*":
                    stack.append(num_1 * num_2)
                elif el == "/":
                    stack.append(int(num_1 / num_2))
        
        return int(stack[-1])
