class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # IDEA: if the current value of height is higher or equal to the previous one,
        #           then the rectangle can keep increasing in the same dimension.
        #       If it is not, it ends there.
        #
        # 1. Keep a stack of pairs: (index, height) where index is the index of the height if a termination is not met
        #       TERMINATION= if the heigth is higher than the next, then a termination is met. Set the inedx as the same 
        #       of the lower or equal going backwards to the left.
        # 2. Pop any pair when it reaches a point where the next height is lower than it is
        # 3. Keep track of a variable for the max area

        max_area: int = 0
        stack = [] # value: (index, heigth)

        for i, h in enumerate(heights):
            start_index = i # We don't know if we can extend it backward yet
            while stack and stack[-1][1] > h:
                # The rectangle can't keep increasing right. Pop it and calculate the area up to now
                index, height = stack.pop()
                # Check if the area can be the highest so far. GOING LEFT
                # The width is the distance between the current column and the one leftmost that is higher or equal.
                # If it is shorter, then the rectangle can't keep increasing left.
                max_area = max(max_area, height * (i - index))
                start_index = index # we know we can extend it backwards bcz it is higher
            stack.append( (start_index, h) )
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area
