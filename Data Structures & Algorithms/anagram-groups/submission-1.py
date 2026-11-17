class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount lo list of Anagrams
        # key: array with number of frequencies for each letter [0 (a), 4 (b), ..., 2 (z)]
        # value: list of strings with that characters' frequencies

        for word in strs:
            char_count = [0] * 26 # a ... z

            for char in word:
                zero_based_index = ord(char) - ord('a') # get [0, 26] index value (ASCII has 2903 e.g.)
                char_count[zero_based_index] += 1
            
            res[tuple(char_count)].append(word)
        
        return list(res.values())