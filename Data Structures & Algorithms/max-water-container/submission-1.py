class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # IDEA: Use two pointers and increment the minimum height value

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