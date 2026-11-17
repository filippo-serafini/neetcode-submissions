class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can keep the whole product of all the elements in the array and then divide it by the i-th
        # number to get the exact value.
        # DRAWBACKS: O(2*n) complexity and Division involved:
        #               if we have two or more zeroes, all the results are 0
        #               if we have zero => only the i-th element with that 0 has a value != 0
        #               no zero => we can simply do safely tot_product // nums[i]

        tot_product = 1
        result = [0] * len(nums)
        zero_cnt = 0
        zero_idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
                zero_idx = i
            else:
                tot_product *= nums[i]

        if zero_cnt == 0:
            for i in range(len(nums)):
                result[i] = tot_product // nums[i]
            return result
        
        if zero_cnt >= 2:
            return result

        if zero_cnt == 1:
            result[zero_idx] = tot_product
            return result
