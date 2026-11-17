class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_1 = {}
        letters_2 = {}

        if len(s) != len(t):
            return False

        # 1. Count how many occurencies for each word's letters
        for i in range(len(s)):
            letters_1[s[i]] = letters_1.get(s[i], 0) + 1
            letters_2[t[i]] = letters_2.get(t[i], 0) + 1
        return letters_1 == letters_2
        