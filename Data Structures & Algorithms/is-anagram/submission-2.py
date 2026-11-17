class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_1 = {} # Dict for the first word
        word_2 = {} # Dict for the second word

        for i in range(len(s)):
            word_1[s[i]] = 1 + word_1.get(s[i], 0)
            word_2[t[i]] = 1 + word_2.get(t[i], 0)

        return word_1 == word_2
        