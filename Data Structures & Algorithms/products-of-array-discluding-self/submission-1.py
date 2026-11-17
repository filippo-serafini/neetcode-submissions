class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix Sum => keep a sum of all the elements before the one involved
        # In this case Prefix & Suffix Mul
        # The result for each i-th element would be just the Pref[i] * Suff[i]

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = 1 # nothing to the left of index 0
        suff[n-1] = 1 # nothing to the right of the last element

        # 1. Build the prefix product array
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

