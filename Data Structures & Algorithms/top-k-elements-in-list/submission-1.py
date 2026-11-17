class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number: occurencies
        freq = [[] for _ in range(len(nums) + 1)] # list of lists where index = freq, value = numbers with that frequency

        # 1. Count occurencies for each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # 2. Group numbers for their frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # Extract the top-k highest frequent numbers
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res