class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        occurencies: int = 0
        best: int = 0

        for num in nums:
            if num == 1:
                occurencies += 1
            else:
                best = max(best, occurencies)
                occurencies = 0
    
        return max(best, occurencies)

        