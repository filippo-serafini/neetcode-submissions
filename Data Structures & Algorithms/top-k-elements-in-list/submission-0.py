class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {} # counts how many times each number appears, num : freq
        freq = [[] for i in range(len(nums) + 1)] # list where index = freq, value = list of nums having that freq.

        for num in nums:
            # Conto quante occorrenze per ogni numero
            num_count[num] = 1 + num_count.get(num, 0)
        for num, cnt in num_count.items():
            # Raggruppo i numeri per occorrenze
            freq[cnt].append(num)

        res = []
        # Devo ciclare a partire dal numero più alto di frequenze => len(nums)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res