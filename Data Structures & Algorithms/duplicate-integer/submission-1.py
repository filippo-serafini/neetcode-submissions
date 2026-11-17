class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Empty set with no duplicates

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False
