class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # HASH SET
        # If a value is present more than once, we only care to find one sequence
        # starting from it. Waste computation if we count multiple times starting from the same number.
        # => With an hash set we eliminate each repetition, having O(1) look-ups.

        nums_set = set(nums) # Eliminate duplicates
        longest = 0 # Longest sequence so far

        
        # Save each start in an hash-set
        for num in nums_set:
            # Check if each number is the beginning of a sequence
            if (num - 1) not in nums_set:
                # It is the start of a sequence. Check the length of it
                length_tmp = 1
                while (num + length_tmp) in nums_set:
                    length_tmp += 1
                longest = max(length_tmp, longest)
            
        
        return longest