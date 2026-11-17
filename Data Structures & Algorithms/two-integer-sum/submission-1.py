class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Think of the condition as complement == target - nums[i] => DIFFERENCES
        complements = {} # dict for the complement that number needs where KEY = Number, VALUE = index in nums

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in complements:
                # That number was looking for nums[i]
                return [complements[diff], i]
            complements[nums[i]] = i
        
        return list()