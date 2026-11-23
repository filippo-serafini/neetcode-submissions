class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # IDEA: The array is sorted and monotonous (non-decreasing order). If we find a couple that is less than target, we know for sure that the left part of the array cannot contain elements suitable for the target. We can discard them. Same thing for the grater sum case/scenario.

        L, R = 0, len(numbers) - 1

        while L < R:
            currSum = numbers[L] + numbers[R]
            if currSum < target:
                L += 1
            elif currSum > target:
                R -= 1
            else:
                return [L+1, R+1]
