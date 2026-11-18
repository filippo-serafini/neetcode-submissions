class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n)
        # MONOTONIC STACK: stack elements in descending order (temperature)
        result = [0] * len(temperatures)

        stack = []  # Store each temperature without warmer days yet.
                    # For each new temperature, check the stack until a lower temp day exists.
        index_stack = [] # Store the index for each temperature in the stack of the original array
        
        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1]:
                # Pop each temperature below the actual temp i
                while stack and stack[-1] < temp:
                    stack.pop()
                    i_res = index_stack.pop()
                    result[i_res] = i - i_res
            stack.append(temp)
            index_stack.append(i)
    
        return result  