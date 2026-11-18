class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # OPTIMIZATION: Sotre tuples instead of keeping two stacks
        result = [0] * len(temperatures)

        stack = []  # Store each (temperature, index) without warmer days yet.
                    # For each new temperature, check the stack until a lower temp day exists.
        
        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                # Pop each temperature below the actual temp i
                while stack and stack[-1][0] < temp:
                    t, index = stack.pop()
                    result[index] = i - index
            stack.append( (temp, i) )
    
        return result  