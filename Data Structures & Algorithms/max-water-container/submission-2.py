class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # IDEA: Use two pointers and move the minimum height value, bcause the width will only decrease so we can find a bigger area only considering higher heights.

        result = 0

        L, R = 0, len(heights) - 1

        while L < R:
            hl, hr = heights[L], heights[R]
            area = (R - L) * min(hl, hr)
            result = max(result, area)

            if hl <= hr:
                L += 1
            elif hr < hl:
                R -= 1

        return result