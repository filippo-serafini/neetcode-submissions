class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #           a + b + c = 0
        # If we fix a -> b + c = -a -> becomes a two sum problem
        result = set()  # To avoid duplicates
        nums.sort()     # To avoid same tuples in different orders


        # 1. Use each number of array as a possible 'a'
        for i, a in enumerate(nums):
            # We don't want the same num to be counted more than once as 'a'
            # We already have an answer (pos or neg) for it
            # nums[i-1] works bcause the input array is sorted
            if i > 0 and a == nums[i-1]:
                continue
            
            # 2. TWO SUM now -- with two pointers
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = a + nums[L] + nums[R]

                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    result.add(tuple([a, nums[L], nums[R]]))
                    # We don't want to check the same numbers again, so we check if nums[L] is already a valid solution
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
    
        return [list(tmp) for tmp in result]