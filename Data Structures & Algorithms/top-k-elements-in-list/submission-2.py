class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occ = {} # occurrencies for each number _ key=num, val=occurr
        # BUCKET SORT: all the numbers with x occurencies go in that index of the array
        freq = [[] for i in range(len(nums) + 1)] # +1 because 

        # 1. Count how many occurencies for each element
        for num in nums:
            num_occ[num] = 1 + num_occ.get(num, 0)
        
        # 2. Group the numbers by their occurency count
        for num, count in num_occ.items():
            freq[count].append(num)
        
        # 3. Get the last-k array of numbers (corresponds to the highest occurencies number)
        result = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result