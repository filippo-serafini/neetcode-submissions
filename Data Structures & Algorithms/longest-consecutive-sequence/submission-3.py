class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Start of a sequence => a number whose n-1 number is not in the array.
        #       Start to count from that number and look for the n+1.
        # 2. We can transform the original array in an HashSet for O(1) lookups

        nums_hs = {} # Key: num, Value: initialise it empty
        longest = 0 # Longest sequence so far

        # Initialise the hash set for O(1) look-ups
        for num in nums:
            nums_hs[num] = 0

        # Check if each number is the beginning of a sequence
        # Save each start in an hash-set
        starts = set() 
        for num in nums:
            if (num - 1) not in nums_hs.keys():
                starts.add(num)
        
        length_tmp = 1
        for start in starts:
            while start + length_tmp in nums_hs.keys():
                length_tmp += 1
            if length_tmp > longest:
                longest = length_tmp
            length_tmp = 0
        
        return longest

        


        

        